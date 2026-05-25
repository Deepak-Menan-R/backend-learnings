# Redis in Web Development

## Table of Contents

* [Introduction](#introduction)
* [What is Redis](#what-is-redis)
* [Why Redis is Needed](#why-redis-is-needed)
* [How Redis Works](#how-redis-works)
* [Redis Architecture](#redis-architecture)
* [Data Structures in Redis](#data-structures-in-redis)
* [Strings](#strings)
* [Lists](#lists)
* [Sets](#sets)
* [Hashes](#hashes)
* [Sorted Sets](#sorted-sets)
* [PubSub](#pubsub)
* [Redis Persistence](#redis-persistence)
* [Redis Caching](#redis-caching)
* [Redis for Sessions](#redis-for-sessions)
* [Redis in Real-Time Applications](#redis-in-real-time-applications)
* [Redis with Node.js](#redis-with-nodejs)
* [Redis Scaling](#redis-scaling)
* [Redis Security](#redis-security)
* [Advantages vs Disadvantages](#advantages-vs-disadvantages)
* [Real-World Example](#real-world-example)
* [Interview Questions](#interview-questions)
* [Key Takeaway](#key-takeaway)

---

# Introduction

Redis is one of the most powerful technologies used in modern web development.

It is widely used for:

* Caching
* Session management
* Real-time systems
* Rate limiting
* Queues
* Pub/Sub messaging
* Leaderboards
* Distributed systems

Many large companies use Redis because it is extremely fast.

---

# What is Redis

Redis stands for:

```text
REmote DIctionary Server
```

Redis is an:

* In-memory database
* Key-value store
* NoSQL database
* Cache system
* Message broker

Unlike traditional databases, Redis stores data primarily in RAM.

This makes Redis extremely fast.

---

# Why Redis is Needed

Modern applications need:

* Fast responses
* Reduced database load
* Real-time communication
* High scalability

Without Redis:

* Databases become overloaded
* APIs become slower
* User sessions become expensive
* Real-time systems become difficult

Redis solves these problems.

---

# How Redis Works

Redis stores data in:

```text
Key → Value
```

Example:

```bash
SET username "Deepak"
GET username
```

Output:

```text
"Deepak"
```

Redis operations are usually:

* O(1) time complexity
* Extremely low latency
* Memory-based

---

# Redis Architecture

```text
Client Application
        │
        ▼
     Redis Server
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
Cache  Sessions Pub/Sub
```

Redis runs as a separate server.

Applications connect using:

* TCP
* Redis protocol

---

# Data Structures in Redis

Redis supports multiple advanced data structures.

| Type        | Description          |
| ----------- | -------------------- |
| String      | Simple value         |
| List        | Ordered collection   |
| Set         | Unique values        |
| Hash        | Object-like storage  |
| Sorted Set  | Ranked values        |
| Bitmap      | Binary operations    |
| HyperLogLog | Approximate counting |
| Stream      | Event streaming      |

---

# Strings

The simplest Redis data type.

## Example

```bash
SET name "Deepak"
GET name
```

## Common Uses

* Cache values
* Tokens
* User sessions
* Counters

## Increment Example

```bash
INCR page_views
```

---

# Lists

Ordered collection of values.

## Example

```bash
LPUSH tasks "Learn Redis"
LPUSH tasks "Learn Node.js"

LRANGE tasks 0 -1
```

## Common Uses

* Queues
* Notification systems
* Task processing

---

# Sets

Stores unique values.

## Example

```bash
SADD skills "React"
SADD skills "Node.js"

SMEMBERS skills
```

## Common Uses

* Tags
* Unique visitors
* Recommendations

---

# Hashes

Stores object-like structures.

## Example

```bash
HSET user:1 name "Deepak"
HSET user:1 role "Developer"

HGETALL user:1
```

## Common Uses

* User profiles
* Product information
* Metadata

---

# Sorted Sets

Stores ranked data.

## Example

```bash
ZADD leaderboard 100 "Alice"
ZADD leaderboard 200 "Bob"

ZRANGE leaderboard 0 -1 WITHSCORES
```

## Common Uses

* Leaderboards
* Rankings
* Gaming systems

---

# Pub/Sub

Redis supports Publish/Subscribe messaging.

## Example

### Publisher

```bash
PUBLISH news "New article released"
```

### Subscriber

```bash
SUBSCRIBE news
```

## Common Uses

* Chat systems
* Live notifications
* Real-time dashboards

---

# Redis Persistence

Redis mainly stores data in memory, but it also supports persistence.

## Persistence Types

| Type | Description     |
| ---- | --------------- |
| RDB  | Snapshot-based  |
| AOF  | Append-only log |

---

## RDB (Redis Database File)

Creates snapshots periodically.

### Advantages

* Faster backups
* Smaller files

### Disadvantages

* Possible data loss between snapshots

---

## AOF (Append Only File)

Logs every write operation.

### Advantages

* Better durability
* Less data loss

### Disadvantages

* Larger file size
* Slightly slower

---

# Redis Caching

Caching is the most common Redis use case.

## Example Architecture

```text
User Request
      │
      ▼
 Application
      │
 ┌────┴────┐
 ▼         ▼
Redis    Database
(Cache)  (Primary)
```

---

## Cache Flow

### Step 1

Application checks Redis.

### Step 2

If data exists:

```text
Cache Hit
```

Return fast response.

### Step 3

If data does not exist:

```text
Cache Miss
```

Fetch from database and store in Redis.

---

## Example

```javascript
const cachedUser = await redis.get("user:1");
```

---

# Redis for Sessions

Redis is commonly used for storing user sessions.

## Why?

Because Redis:

* Is fast
* Supports expiration
* Handles millions of sessions

## Example

```bash
SET session:123 "user_data" EX 3600
```

This expires after:

```text
3600 seconds
```

---

# Redis in Real-Time Applications

Redis is widely used in:

| Application Type | Usage              |
| ---------------- | ------------------ |
| Chat Apps        | Message delivery   |
| Gaming           | Leaderboards       |
| Trading Systems  | Live market data   |
| Analytics        | Real-time counters |
| Notifications    | Pub/Sub            |
| IoT              | Device messaging   |

---

# Redis with Node.js

Redis works extremely well with Node.js.

## Installation

```bash
npm install redis
```

## Example

```javascript
import { createClient } from "redis";

const client = createClient();

await client.connect();

await client.set("name", "Deepak");

const value = await client.get("name");

console.log(value);
```

---

# Redis Scaling

Redis supports scaling using:

| Feature     | Purpose            |
| ----------- | ------------------ |
| Replication | Read scaling       |
| Clustering  | Horizontal scaling |
| Sharding    | Data distribution  |
| Sentinel    | High availability  |

---

# Replication

Creates read replicas.

```text
Master → Replica
```

Benefits:

* Faster reads
* Backup support
* Fault tolerance

---

# Redis Cluster

Redis Cluster distributes data across multiple nodes.

Benefits:

* Horizontal scaling
* Better performance
* Large datasets

---

# Redis Sentinel

Sentinel provides:

* Monitoring
* Automatic failover
* High availability

---

# Redis Security

Redis should never be exposed publicly without protection.

## Best Practices

* Use authentication
* Enable firewalls
* Use TLS encryption
* Restrict network access
* Disable dangerous commands

---

# Advantages vs Disadvantages

| Advantages                    | Disadvantages                 |
| ----------------------------- | ----------------------------- |
| Extremely fast                | RAM expensive                 |
| Easy caching                  | Memory limitations            |
| Supports many data structures | Persistence weaker than SQL   |
| Great for real-time systems   | Complex scaling               |
| Simple API                    | Not ideal for relational data |

---

# Real-World Example

## E-Commerce Website

### Redis Uses

| Feature       | Redis Usage          |
| ------------- | -------------------- |
| User Sessions | Fast session storage |
| Product Cache | Faster product pages |
| Cart System   | Temporary cart data  |
| Rate Limiting | API protection       |
| Notifications | Real-time alerts     |
| Leaderboards  | Top-selling products |

---

# Redis vs SQL Database

| Feature     | Redis             | SQL DB            |
| ----------- | ----------------- | ----------------- |
| Storage     | In-memory         | Disk-based        |
| Speed       | Extremely fast    | Slower            |
| Data Model  | Key-value         | Relational        |
| Persistence | Limited           | Strong            |
| Best Use    | Cache & real-time | Permanent storage |

---

# Redis vs Memcached

| Feature         | Redis    | Memcached        |
| --------------- | -------- | ---------------- |
| Data Structures | Advanced | Simple key-value |
| Persistence     | Yes      | No               |
| Pub/Sub         | Yes      | No               |
| Replication     | Yes      | Limited          |

---

# Interview Questions

## Q: Why is Redis fast?

Because Redis stores data primarily in RAM.

---

## Q: What is Redis mainly used for?

Caching, sessions, queues, real-time systems, and Pub/Sub messaging.

---

## Q: What is cache hit and cache miss?

* Cache Hit → Data found in Redis
* Cache Miss → Data not found, fetch from database

---

## Q: Difference between Redis and MongoDB?

Redis is mainly an in-memory key-value store, while MongoDB is a document database designed for persistent storage.

---

## Q: What is Redis Pub/Sub?

A messaging system where publishers send messages and subscribers receive them in real time.

---

## Q: What is Redis persistence?

Mechanisms that allow Redis data to survive server restarts using RDB or AOF.

---

## Q: Why use Redis for sessions?

Because it is fast and supports automatic expiration.

---

# Key Takeaway

Redis is one of the most important technologies in scalable web applications.

Modern systems use Redis for:

* Caching
* Sessions
* Queues
* Real-time messaging
* Rate limiting
* Distributed systems

Redis is not usually a replacement for SQL databases.

Instead:

```text
SQL Database + Redis
```

is one of the most common architectures in modern backend development.

Understanding Redis is essential for backend and full-stack developers.

✨ End of Notes
