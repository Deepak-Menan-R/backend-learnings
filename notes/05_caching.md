# Day 05 – Caching in Backend Systems

## ⚡ What is Caching?

**Caching** is the practice of storing frequently accessed data in a **fast-access storage layer**  
to reduce latency and avoid repeated expensive computations or database queries.

Goal:

👉 Serve responses faster  
👉 Reduce backend load  
👉 Improve scalability  

---

## 🧠 Why Caching is Important

Without caching:

- Every request hits the database
- Increased latency
- Higher server load

With caching:

- Faster responses
- Reduced DB queries
- Better performance

---

## 🚀 Benefits of Caching

✔ Reduced response time  
✔ Lower database load  
✔ Improved throughput  
✔ Better user experience  
✔ Cost efficiency  

---

## 📦 What Can Be Cached?

Common candidates:

- Database query results
- API responses
- Computed values
- Configuration data
- Session data
- Static resources

---

## 🔁 Basic Caching Flow

1️⃣ Client sends request  
2️⃣ Server checks cache  

- If cache HIT → Return cached data  
- If cache MISS → Fetch from DB → Store in cache → Return  

---

## 🎯 Cache Hit vs Cache Miss

### ✅ Cache Hit
Data found in cache → Instant response

### ❌ Cache Miss
Data not found → Backend computation / DB query needed

---

## 🏗 Example Scenario

Endpoint:

GET /products/10


Without caching:

→ Query DB every time

With caching:

→ First request → DB  
→ Subsequent requests → Cache  

---

## 🛠 Practical Example (Conceptual)

### Cache Lookup Logic

IF data exists in cache
RETURN cached response

ELSE
FETCH data from database
STORE data in cache
RETURN response


---

## 🧩 Types of Caching

### ✅ In-Memory Cache

Stored inside application memory.

Examples:

- Python dictionary
- Local memory store

**Pros**
- Extremely fast
- Simple

**Cons**
- Lost on restart
- Not shared across servers

---

### ✅ Distributed Cache

Separate caching system shared across services.

Examples:

- Redis
- Memcached

**Pros**
- Scalable
- Persistent (optional)
- Shared

---

## ⏳ Cache Expiration (TTL)

**TTL (Time To Live)** defines how long data stays cached.

Example:

- Cache user profile for 5 minutes
- Cache product list for 1 hour

Prevents:

❌ Stale data issues  

---

## 🔄 Cache Invalidation (CRITICAL CONCEPT)

Removing outdated cache entries.

Triggered when:

- Data updates
- Data deletes
- TTL expiry

Common strategies:

✔ Time-based expiration  
✔ Write-through  
✔ Write-back  
✔ Manual invalidation  

---

## ⚠️ Stale Data Problem

Cached data may not reflect latest DB state.

Solution:

✔ Proper TTL  
✔ Smart invalidation  

---

## 🛡 When NOT to Cache

Avoid caching:

❌ Highly dynamic data  
❌ Sensitive data (unless secured)  
❌ Real-time critical values  

---

## 🚀 Caching Best Practices

✔ Cache frequently read data  
✔ Use appropriate TTL  
✔ Design invalidation strategy  
✔ Avoid over-caching  
✔ Monitor cache performance  

---

## 🎯 Interview Questions

**Q: What is caching?**

Storing frequently accessed data in fast storage to improve performance.

---

**Q: Cache hit vs miss?**

Hit → Data in cache  
Miss → Data fetched from backend

---

**Q: Why use Redis?**

✔ Fast  
✔ Distributed  
✔ Persistent  
✔ Scalable  

---

**Q: What is TTL?**

Defines cache lifetime.

---

**Q: Hardest part of caching?**

👉 Cache invalidation 😄

---

## ✅ Key Takeaway

Caching improves:

✔ Performance  
✔ Scalability  
✔ Response speed  

But requires:

✔ Expiration strategy  
✔ Invalidation logic  