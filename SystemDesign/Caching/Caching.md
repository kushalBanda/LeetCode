## What is Caching?

A cache is just a temporary storage that keeps recently used data handy so you can get it much faster next time.

### When to Bring Up Caching?

Bring up caching when you're hitting the same data repeatedly. If 80% of requests fetch the same 20% of data, that's a perfect caching opportunity. Database queries taking too long? API calls slowing you down? Users complaining about load times? Time to cache.

**Don't cache** everything blindly. Caching adds complexity—stale data, invalidation logic, memory costs. Cache what hurts without it: expensive database queries, external API calls, computed results.

![When to Bring Up Caching](assets/When%20to%20Bring%20Up%20Caching.png)

### Caching in Memory

In-memory caches store data in RAM instead of disk. RAM is 100-1000x faster than SSD, which is why Redis and Memcached can serve millions of requests per second. The trade-off: RAM is expensive and volatile—if the server restarts, the cache is gone.

**Production reality:** Redis dominates production caching. It's fast, supports data structures (lists, sets, sorted sets), and has built-in persistence options. Memcached is simpler and slightly faster for pure key-value caching, but Redis's features usually win out.

![Caching](assets/Caching.png)

### Where to Cache

#### Client-side Caching

Store data in the browser (localStorage, sessionStorage, IndexedDB) or mobile app. Fastest possible cache—zero network latency. Perfect for user preferences, recently viewed items, or data that doesn't change often.

**When to use:** Static assets (images, CSS, JS), user settings, offline-first apps. PWAs (Progressive Web Apps) rely heavily on client-side caching.

**Production reality:** Every major website caches static assets in your browser with HTTP cache headers. Mobile apps cache user data locally to work offline. Gmail caches emails, Spotify caches songs, Netflix caches video chunks.

![Client-side Caching](assets/Where%20to%20cache/Client-side%20Caching.png)

#### In-Process Caching

Cache stored in your application's memory—same process, no network hop. Blazing fast but only available to that single server instance. If you have 10 app servers, each has its own cache.

**When to use:** Single-server apps, caching computed values, configuration data. Anything where network latency to an external cache would hurt more than help.

**Production reality:** Most web frameworks include in-process caching (Rails cache, Flask caching, Node.js LRU cache). It's the first caching layer you add. But if you scale horizontally (multiple servers), you'll need external caching for shared state.

![In-Process Caching](assets/Where%20to%20cache/In-Process%20Caching.png)

#### External Caching

Dedicated caching server (Redis, Memcached) that all your app servers share. Adds network latency but gives you consistent caching across a cluster. Scale your cache independently from your app servers.

**When to use:** Multi-server deployments, session storage, distributed systems. Anytime you need cache consistency across multiple app instances.

**Production reality:** This is the standard caching layer for production apps. Twitter, Instagram, and Pinterest run massive Redis clusters. Amazon's ElastiCache is just managed Redis/Memcached. Every scaled app eventually moves to external caching.

![External Caching](assets/Where%20to%20cache/External%20Caching.png)

#### Content Delivery Network (CDN)

Caching servers spread across the globe. When a user in Tokyo requests your image, the CDN serves it from Tokyo, not from your server in Virginia. Cuts latency from 200ms to 20ms.

**When to use:** Static assets (images, videos, CSS, JavaScript), downloadable files, API responses that don't change often. Any content that's the same for all users.

**Production reality:** Every major site uses CDNs. Netflix streams through CDN nodes. Facebook caches images and videos at edge locations. Cloudflare caches 11 trillion requests per month. If you're serving static assets without a CDN, you're leaving performance on the table.

![CDN](assets/Where%20to%20cache/CDN.png)

### Cache Architecture

#### Cache-Aside

Also called "lazy loading." Your app checks the cache first. If the data's there (cache hit), return it. If not (cache miss), fetch from the database, store it in cache, then return it. The app controls all caching logic.

**When to use:** Most applications. It's the default pattern because it's simple and the app has full control over what gets cached.

**Production reality:** This is how most teams start caching. Memcached and Redis are built for cache-aside. The pattern is simple but watch out for cache stampedes (see Common Issues below).

![Cache-Aside](assets/Cache%20Architecture/1.%20Cache-Aside.png)

#### Read-through

The cache sits in front of the database. Your app always talks to the cache, never directly to the database. On a cache miss, the cache itself fetches from the database, stores it, then returns it. The app doesn't know where data comes from.

**When to use:** When you want to abstract away caching logic from the app. The cache layer handles all the details.

**Production reality:** Less common than cache-aside because it requires a smarter cache layer. AWS DynamoDB Accelerator (DAX) uses read-through caching. Most teams stick with cache-aside because it's more flexible.

![Read-through](assets/Cache%20Architecture/4.%20Read-through.png)

#### Write-through

Write to the cache and database at the same time. Every write hits both systems before returning success. Keeps cache always fresh but adds latency to writes.

**When to use:** When you can't tolerate stale data and write latency isn't critical. Financial systems, inventory management, anything where cache and database must stay in sync.

**Production reality:** Rare in pure form because synchronous dual writes are slow. DynamoDB Accelerator (DAX) supports it. Most teams use write-through for critical data and cache-aside for everything else.

![Write-through](assets/Cache%20Architecture/2.%20Write-through.png)

#### Write-behind

Also called "write-back." Write to the cache immediately and return success. The cache writes to the database asynchronously in the background. Fast writes but risky—if the cache crashes before flushing to the database, you lose data.

**When to use:** High-write workloads where you can tolerate some data loss risk. Logging, analytics, metrics collection.

**Production reality:** Rare because the data loss risk scares most teams. Some databases (MySQL with InnoDB buffer pool) use write-behind internally, but apps rarely configure it explicitly. If you need fast writes, consider message queues instead.

![Write-behind](assets/Cache%20Architecture/3.%20Write-behind.png)

### Cache Eviction Policies

Caches have limited memory. When full, they need to evict (remove) items to make room. The eviction policy decides what goes.

**LRU (Least Recently Used):** Evict the item that hasn't been accessed in the longest time. Works great when recent data is hot. Redis and Memcached default to LRU variants.

**LFU (Least Frequently Used):** Evict the item accessed the fewest times. Good when some data is consistently popular. Harder to implement than LRU.

**FIFO (First In First Out):** Evict the oldest item. Simple but dumb—doesn't consider access patterns at all.

**TTL (Time to Live):** Items expire after a set time. Not strictly eviction, but solves cache staleness. Most production caches combine LRU with TTL.

**Production reality:** Redis supports LRU, LFU, and random eviction. Most teams use LRU because it's a good default. Add TTLs to prevent stale data. Don't overthink it—LRU + TTL handles 95% of cases.

![Cache Eviction Policies](assets/Cache%20Eviction%20Policies/Cache%20Eviction%20Policies.png)

### Common Issues

#### Cache Stampede (Thundering Herd)

A popular cache key expires. Suddenly 1,000 concurrent requests all get cache misses and hit the database at once. Database gets crushed.

**Solutions:**

- **Locking:** First request to miss the cache gets a lock and fetches data. Other requests wait for the lock. Prevents duplicate database queries.
- **Probabilistic early expiration:** Refresh cache before it expires, based on load and TTL. If TTL is 60s and 59s have passed, refresh it early.
- **Stale-while-revalidate:** Serve stale cached data while fetching fresh data in the background.

**Production reality:** Facebook and Twitter have been hit by cache stampedes during major events. Redis supports distributed locks (SETNX). Most teams add jitter to TTLs (random +/- 10%) to spread out expirations.

![Cache Stampede](assets/Common%20Issues/1.%20Cache%20Stampede%20(Thundering%20Herd).png)

#### Cache Consistency

Database and cache get out of sync. User updates their profile in the database, but the cache still has the old data. You're serving stale data.

**Solutions:**

- **Cache invalidation:** Delete the cache key when you update the database. Next read will cache miss and fetch fresh data.
- **TTL:** Let cache entries expire automatically. Short TTLs (1-5 minutes) for data that changes often.
- **Write-through caching:** Update cache and database together (see Cache Architecture above).
- **Change Data Capture (CDC):** Listen to database changes and invalidate cache automatically. Tools like Debezium do this.

**Production reality:** Cache invalidation is the hardest part of caching. "There are only two hard things in Computer Science: cache invalidation and naming things." Most teams use TTLs + manual invalidation on writes. For critical data, use short TTLs or skip caching entirely.

![Cache Consistency](assets/Common%20Issues/2.%20Cache%20Consistency.png)

#### Hot Keys

A single cache key gets hammered with requests. Maybe a celebrity's profile, a trending tweet, or a product page during a flash sale. That one Redis server (or shard) becomes a bottleneck.

**Solutions:**

- **Replication:** Replicate hot keys across multiple cache servers. Read from replicas to distribute load.
- **Local caching:** Cache hot keys in-process (application memory) to avoid hitting Redis for every request.
- **Request coalescing:** Multiple concurrent requests for the same key share a single cache fetch.

**Production reality:** Twitter's cache gets slammed during trending events. Instagram replicates celebrity profile data. Netflix caches popular show thumbnails aggressively. If one cache key is >10% of your traffic, it's a hot key problem.

![Hot Keys](assets/Common%20Issues/3.%20Hot%20Keys.png)
