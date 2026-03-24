# Day 33 – Distributed Caching

## ⚡ What is Distributed Caching?

**Distributed caching** is a caching technique where cached data is stored across multiple machines (nodes) instead of a single server.

Unlike local/in-memory cache (single instance), distributed cache is **shared across multiple application instances**.

Goal:

- Improve performance
- Reduce database load
- Enable scalability
- Share cache across services

---

## 🧠 Why Distributed Caching is Important

In scalable systems:

- Multiple backend servers handle requests
- Each server cannot maintain its own isolated cache

Without distributed cache:

❌ Cache inconsistency  
❌ Duplicate database queries  
❌ Poor cache utilization  

With distributed cache:

✔ Shared cache across services  
✔ Reduced DB load  
✔ Faster responses  
✔ Better scalability  

---

## 📦 Basic Architecture


Client → Application Servers → Distributed Cache → Database


Example:


Client
|
App Server 1 ─┐
App Server 2 ─┼── Redis Cluster ── Database
App Server 3 ─┘


All servers access the same cache layer.

---

## 🔁 How Distributed Cache Works

1️⃣ Request comes to application  
2️⃣ Check cache  

- If HIT → Return cached data  
- If MISS → Fetch from DB → Store in cache  

---

## 🎯 Cache Hit vs Cache Miss

### Cache Hit

✔ Data found in cache  
✔ Fast response  

---

### Cache Miss

❌ Data not in cache  
✔ Fetch from DB  
✔ Store in cache  

---

## 🧩 Types of Distributed Cache

### 1️⃣ In-Memory Distributed Cache

Stored in RAM across multiple nodes.

Examples:

- Redis
- Memcached

✔ Very fast  
❌ Limited by memory  

---

### 2️⃣ Persistent Cache

Cache stored with persistence support.

Example:

- Redis with disk persistence

✔ Data survives restarts  

---

## ⚙ Common Caching Strategies

---

### 1️⃣ Cache Aside (Lazy Loading)

Application manages cache.

Flow:


IF cache miss
Fetch from DB
Store in cache


✔ Most commonly used  

---

### 2️⃣ Write Through

Data written to cache and DB simultaneously.


Write → Cache + Database


✔ Strong consistency  

---

### 3️⃣ Write Back (Write Behind)

Write only to cache, later persisted to DB.

✔ Faster writes  
❌ Risk of data loss  

---

### 4️⃣ Read Through

Cache automatically loads data from DB.

---

## ⚠ Cache Invalidation (Hard Problem)

When underlying data changes:

❌ Cached data becomes stale  

Solution:

✔ TTL (Time-To-Live)  
✔ Manual invalidation  
✔ Event-based updates  

---

## ⏳ TTL (Time-To-Live)

Defines how long data stays in cache.

Example:


Cache expires after 5 minutes


Prevents stale data issues.

---

## 🚀 Benefits of Distributed Caching

✔ Faster response times  
✔ Reduced database load  
✔ Improved scalability  
✔ High availability  

---

## ⚠ Challenges

❌ Cache consistency  
❌ Cache invalidation  
❌ Memory limitations  
❌ Network overhead  

---

## 🛠 Popular Distributed Cache Systems

- Redis
- Memcached
- Hazelcast
- Apache Ignite

---

## ⚠ Common Mistakes

❌ Not handling cache invalidation  
❌ Over-caching everything  
❌ No TTL strategy  
❌ Caching sensitive data  

---

## 🎯 Interview Questions

**Q: What is distributed caching?**

Caching data across multiple nodes accessible by multiple services.

---

**Q: Why not use local cache?**

Because it is not shared across servers and causes inconsistency.

---

**Q: What is cache aside strategy?**

Application loads data into cache on demand.

---

**Q: What is TTL?**

Time after which cache expires.

---

## ✅ Key Takeaway

Distributed caching is essential for:

✔ High-performance systems  
✔ Scalable architectures  
✔ Efficient data access  

It reduces load on databases and improves response times significantly.

✨ End of Day 33