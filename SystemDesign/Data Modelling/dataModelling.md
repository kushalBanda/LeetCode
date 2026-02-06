## Database Model Options

### 1. Relational Database

Tables with rows and columns. Data is structured and relationships are enforced through foreign keys. SQL is the query language. ACID guarantees mean your data stays consistent—no partial writes, no lost transactions.

**When to use:** Structured data with complex relationships. Financial systems, e-commerce orders, user management. Anything where data integrity matters more than raw speed.

**Production reality:** PostgreSQL, MySQL, Oracle. Still the default choice for most applications. Every startup begins with a relational database. The structure forces you to think through your data model upfront, which prevents chaos later.

**Trade-offs:** Schema changes are painful at scale. Adding a column to a billion-row table can lock the database for hours. Horizontal scaling is hard—sharding requires careful planning.

![Relational DB](assets/Relational%20DB.png)
### 2. Document Databases

Store data as JSON-like documents. No fixed schema—each document can have different fields. Query by any field in the document. Perfect for hierarchical data that doesn't fit neatly into tables.

**When to use:** Content management, user profiles, product catalogs. Data that naturally groups together (a blog post with comments, a user with preferences and history).

**Production reality:** MongoDB dominates this space. Contentful, Medium, and Lyft use MongoDB. AWS DocumentDB is MongoDB-compatible. Document databases won because they match how developers think—objects, not tables.

**Trade-offs:** No enforced schema means no safety net. You can accidentally save inconsistent data. Joins are weak or nonexistent—you'll denormalize data and duplicate it across documents.

![Document DB](assets/Document%20DB.png)
### 3. Key-Value Store

The simplest database model. Store a value (string, JSON, binary) under a key. Retrieve it by key. That's it. No queries, no indexes on values, no joins. But it's incredibly fast—millions of operations per second.

**When to use:** Caching, session storage, real-time leaderboards, rate limiting. Anything where you always look up by key and need sub-millisecond latency.

**Production reality:** Redis and Memcached. Every scaled application uses Redis for caching. Twitter uses Redis for timeline storage. GitHub uses Redis for job queues. If you need speed and your access pattern is key-based, nothing beats key-value stores.

**Trade-offs:** You can only query by key. No "give me all users in California" unless you maintain a separate index. Data modeling becomes your responsibility.

![Key Value](assets/Key%20Value.png)
### 4. Wide-Column Store

Like a key-value store, but values are organized into columns. Each row can have different columns—no fixed schema. Optimized for reading and writing massive amounts of data across distributed systems.

**When to use:** Time-series data, analytics, IoT sensors, event logging. Anything with high write throughput and queries that scan many rows but only a few columns.

**Production reality:** Cassandra, HBase, Google Bigtable (which inspired both). Netflix uses Cassandra to store viewing history. Apple uses Cassandra for billions of rows. Wide-column stores scale horizontally like crazy—add servers to handle more data.

**Trade-offs:** Complex to operate. Query capabilities are limited compared to SQL. You need to design your schema around your queries—can't just add an index later like in relational databases.

![Wide Column DB](assets/Wide%20Column%20DB.png)
### 5. Graph Database

Data is stored as nodes (entities) and edges (relationships). Built for traversing connections. If your queries ask "who's connected to whom?" or "what's the shortest path?", graphs are 1000x faster than relational joins.

**When to use:** Social networks, recommendation engines, fraud detection, knowledge graphs. Anything where relationships are as important as the entities themselves.

**Production reality:** Neo4j dominates. LinkedIn uses graph databases for their connections network. Facebook built TAO (their graph database) for the social graph. Airbnb uses graphs for search and recommendations.

**Trade-offs:** Overkill if you're not doing heavy relationship queries. Scaling graph databases is hard—relationships make sharding complex. Most apps don't need graphs.

![Graph DB](assets/Graph%20DB.png)

## Schema Design

Your schema is your blueprint. Get it wrong and you'll spend years refactoring. Three factors drive every schema decision:

1. **Data volume:** Single server or distributed cluster? Billions of rows need sharding.
2. **Access patterns:** How will you query this data? Queries drive indexes and structure.
3. **Consistency requirements:** Can you tolerate stale data, or do you need ACID guarantees?

Design for your access patterns, not your entity model. If 90% of queries are "get user's recent posts," denormalize posts into the user document. Don't fight your database's strengths.

### Entities, Keys & Relationships

Entities are your nouns (users, posts, comments). Keys identify them uniquely (user_id, post_id). Relationships connect them (one-to-many, many-to-many).

**Relational databases** enforce relationships with foreign keys. **NoSQL databases** leave relationships to your application code—you'll either embed related data (denormalization) or manually join it in code.

**Primary keys** must be unique and stable. Auto-increment integers work for single servers but break with distributed databases. Use UUIDs or Twitter Snowflake IDs for distributed systems.

![Entities, Key & Relationships](assets/Entities,%20Key%20&%20Relationships.png)
### Normalization vs Denormalization

**Normalization:** Split data into separate tables to eliminate duplication. User data lives in `users`, posts in `posts`. Changes to a user's name only update one row. Enforces consistency but requires joins.

**Denormalization:** Duplicate data to avoid joins. Store the author's name directly in the `posts` table. Reads are fast (no joins), but updates are expensive—change a username and you update thousands of post records.

**The rule:** Normalize by default in relational databases. Denormalize when read performance matters more than write complexity. In NoSQL, denormalization is often the default because joins are weak or missing.

**Production reality:** Most teams start normalized, then selectively denormalize hot paths. Facebook denormalizes heavily—profile data is duplicated across many systems to avoid joins. But they pay the cost in complexity.

![Normalization vs Denormalization](assets/Normalization%20vs%20Denormalization.png)
### Indexing

Indexes make queries fast by creating lookup tables. Without an index on `email`, finding a user by email requires scanning every row (slow). With an index, it's a binary search (fast).

**The trade-off:** Indexes speed up reads but slow down writes. Every INSERT, UPDATE, or DELETE must update all relevant indexes. Too many indexes and writes crawl.

**What to index:**

- Primary keys (automatic)
- Foreign keys used in joins
- Columns in WHERE clauses you run frequently
- Columns used for sorting (ORDER BY)

**What not to index:**

- Low-cardinality columns (boolean flags with only true/false)
- Columns that change constantly (write-heavy workloads)
- Small tables (under 1000 rows—full scans are fine)

**Production reality:** Most query performance problems come from missing indexes. Add an index on `user_id` and your query goes from 5 seconds to 5 milliseconds. But every index costs memory and write performance. Profile your queries and index what hurts.

![Indexing](assets/Indexing.png)
### Scaling and Sharding

**Vertical scaling:** Bigger server. More RAM, faster CPU, bigger disk. Simple but hits limits around $50k/month for hardware.

**Horizontal scaling (sharding):** Split data across multiple servers. Users 1-1M on server A, 1M-2M on server B. Each server (shard) handles a portion of the data.

**Sharding strategies:**

- **Hash-based:** Hash the user_id and use modulo to pick a shard. Even distribution but you can't easily add servers.
- **Range-based:** Users A-M on shard 1, N-Z on shard 2. Easy to add shards but can cause hotspots.
- **Geographic:** US users on US servers, EU users on EU servers. Great for latency, bad if usage is unbalanced.

**The pain:** Sharding breaks features. No cross-shard joins. No cross-shard transactions. Count queries become expensive (query every shard and sum). You'll need a strategy for aggregating data.

**Production reality:** Most apps never need sharding. Start with a single beefy PostgreSQL server—modern hardware handles millions of rows fine. Instagram ran on a single database for years. When you do shard, pick your shard key carefully—it's almost impossible to change later.

![Scaling and Sharding](assets/Scaling%20and%20Sharding.png)

## Summary

Pick the right database for your access patterns:

- **Relational:** Structured data, complex queries, ACID guarantees
- **Document:** Flexible schema, nested data, developer-friendly
- **Key-value:** Caching, sessions, blazing speed
- **Wide-column:** Time-series, high write throughput, massive scale
- **Graph:** Relationships and connections

Design your schema for how you'll query it, not how the data "should" be structured. Normalize for consistency, denormalize for speed. Index what hurts. Shard only when you must.

Most importantly: start simple. You can always migrate to a more complex setup later. But you can't undo a premature sharding decision.

![Wrapping up](assets/Wrapping%20up.png)

