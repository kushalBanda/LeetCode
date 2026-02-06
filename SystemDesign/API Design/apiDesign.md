# API Design

## Overview

![API Design](assets/API.png)

## REST Architecture

The web's native API style. REST uses standard HTTP methods (GET, POST, PUT, DELETE) and treats everything as a resource with a URL. Simple, stateless, and cacheable by default.

**When to use:** Public APIs, web services, CRUD operations. If you're building a standard web API and don't have special requirements, start here.

**Production reality:** Twitter, GitHub, Stripe, and most SaaS companies expose REST APIs. It's the default choice because every HTTP client understands it out of the box.

![REST](assets/REST.png)

## HTTP Methods

The verbs of REST APIs. GET fetches data, POST creates it, PUT/PATCH updates it, DELETE removes it. Each method has specific semantics—GET must be safe (read-only), PUT must be idempotent (calling it twice does the same thing as calling it once).

**Production reality:** Most APIs stick to GET, POST, PUT, and DELETE. PATCH exists for partial updates, but many teams just use PUT. HEAD and OPTIONS are mainly for CORS and performance checks. You won't see CONNECT or TRACE in typical REST APIs.

![HTTP Methods](assets/HTTP%20Methods.png)

## Responses

HTTP status codes tell clients what happened. 2xx means success, 3xx means redirect, 4xx means client screwed up, 5xx means server screwed up. The most common: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Server Error.

**Production reality:** Don't overthink this. Most APIs use 200, 201, 400, 401, 403, 404, and 500. You don't need all 70+ HTTP status codes. Pick the handful that clearly communicate success, client error, or server error.

Response bodies should be consistent—always JSON with the same structure. Include error messages that actually help developers debug issues, not generic "An error occurred."

![Responses](assets/Responses.png)

## GraphQL

A query language for APIs. Clients specify exactly what data they need in a single request. No more fetching `/users/123`, then `/users/123/posts`, then `/posts/456/comments`. One query gets all related data in one shot.

**When to use:** Complex front-ends that need flexible data fetching. Mobile apps where bandwidth matters. Apps with lots of nested relationships.

**Production reality:** Facebook invented it and uses it everywhere. GitHub, Shopify, and Netflix use GraphQL for their public APIs. But it's overkill for simple CRUD apps—the learning curve and backend complexity aren't worth it unless you're fighting over-fetching or under-fetching problems with REST.

**Trade-off:** GraphQL solves client flexibility but adds server complexity. You need a GraphQL server, schema definition, resolver functions, and query cost analysis to prevent clients from writing expensive queries. REST is simpler if your API needs are straightforward.

![GraphQL](assets/GraphQL.png)

## RPC

Remote Procedure Call—calling a function on another machine like it's local code. Unlike REST's resource-based approach, RPC is action-based: `createUser()`, `sendEmail()`, `processPayment()`. gRPC is the modern standard, using Protocol Buffers for serialization and HTTP/2 for transport.

**When to use:** Internal microservices, high-performance APIs, real-time systems. If you need type safety, streaming, or sub-millisecond latency between services.

**Production reality:** Google runs everything on gRPC internally. Netflix, Square, and Uber use it for service-to-service communication. It's faster and more efficient than REST/JSON, but the tooling is heavier and it's harder to debug (binary protocol instead of readable JSON).

**Trade-off:** gRPC gives you performance and type safety, but REST gives you simplicity and universal compatibility. For public APIs, REST wins. For internal microservices that need speed, gRPC wins.

![RPC](assets/RPC.png)

## Pagination

Never return all 10 million rows at once. Pagination breaks large result sets into chunks. Three main approaches: offset-based (`?page=3&limit=20`), cursor-based (opaque token pointing to your position), and keyset pagination (filter by last seen ID).

**Offset pagination:** Simple but slow on large datasets. Skipping the first 1 million rows (`OFFSET 1000000`) makes the database scan all those rows.

**Cursor pagination:** Fast and consistent. Cursors are opaque tokens—the client doesn't need to understand them. Works even when data changes between requests. This is what Stripe, Twitter, and Facebook use.

**Keyset pagination:** Uses the last record's ID for the next query (`WHERE id > 12345 LIMIT 20`). Fast and works with database indexes, but you can't jump to arbitrary pages.

**Production reality:** Use cursor or keyset pagination for anything past a few thousand rows. GitHub's API uses cursor pagination. Stripe uses cursor pagination. Twitter's API uses cursor pagination. Offset pagination is only for small datasets or admin tools where you need page numbers.

![Pagination](assets/Pagination.png)

## Security

APIs are attack surfaces. You need authentication (who are you?), authorization (what can you do?), encryption (HTTPS), and rate limiting (stop abuse).

**Authentication:** OAuth 2.0 for third-party apps, JWT tokens for session management, API keys for server-to-server. Never roll your own auth—use proven libraries.

**Authorization:** Check permissions on every request. Don't trust client-side checks. A user's JWT might say they're an admin, but verify it server-side before deleting data.

**Rate limiting:** Prevent abuse and DDoS. GitHub allows 5,000 requests/hour for authenticated users, 60/hour for unauthenticated. Stripe uses sliding windows to smooth out bursts.

**Production reality:** Every production API runs on HTTPS (not HTTP). Most use OAuth 2.0 or JWTs for auth. All major APIs (AWS, Stripe, Twilio) use API keys for authentication and rate limiting to prevent abuse. If your API is public, add rate limiting from day one—you'll get hammered by bots otherwise.

![Security](assets/Security.png)
