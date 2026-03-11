# Day 22 – Database Sharding

## 🗂 What is Database Sharding?

**Database sharding** is the technique of splitting a large database into smaller, more manageable pieces called **shards**.

Each shard contains a subset of the total data and runs on a separate database server.

Goal:

- Improve scalability
- Handle large datasets
- Increase performance
- Distribute load across multiple servers

---

## 🧠 Why Sharding is Needed

As applications grow, databases face challenges:

❌ Large datasets  
❌ Slow queries  
❌ High write traffic  
❌ Hardware limits  

Scaling a single database server vertically has limits.

Sharding allows **horizontal scaling** by distributing data across multiple servers.

---

## 📦 Basic Sharding Architecture


Application
|
Router
/ |
DB1 DB2 DB3


Example:

- Shard 1 → Users 1–1,000,000  
- Shard 2 → Users 1,000,001–2,000,000  
- Shard 3 → Users 2,000,001–3,000,000  

Each database stores only a portion of the total dataset.

---

## 🔑 Shard Key

A **shard key** determines how data is distributed across shards.

Example shard key:


user_id


The system uses the shard key to decide which shard stores the data.

Example:


user_id % 3


Result determines shard location.

---

## 🧩 Sharding Strategies

### 1️⃣ Range-Based Sharding

Data divided by value ranges.

Example:


Shard1 → user_id 1–1000
Shard2 → user_id 1001–2000
Shard3 → user_id 2001–3000


Pros:

✔ Simple implementation  

Cons:

❌ Uneven load if ranges are not balanced.

---

### 2️⃣ Hash-Based Sharding

Shard determined using a hash function.

Example:


hash(user_id) % number_of_shards


Pros:

✔ Even distribution of data  

Cons:

❌ Harder to rebalance shards.

---

### 3️⃣ Directory-Based Sharding

A lookup table determines shard location.

Example:


UserID → Shard mapping table


Pros:

✔ Flexible shard placement  

Cons:

❌ Extra lookup required.

---

## 🚀 Benefits of Sharding

✔ Horizontal scalability  
✔ Improved performance  
✔ Reduced query load per server  
✔ Better handling of large datasets  

---

## ⚠ Challenges of Sharding

❌ Complex architecture  
❌ Difficult cross-shard queries  
❌ Data rebalancing challenges  
❌ Increased operational complexity  

---

## 🔁 Example Use Case

Large social media platform:


User Service → Sharded Database


Each shard stores data for a subset of users.

Example:


Shard1 → Users in region A
Shard2 → Users in region B
Shard3 → Users in region C


---

## ⚠ Cross-Shard Queries

Queries requiring data from multiple shards are complex.

Example:


SELECT COUNT(*) FROM users;


The system must query every shard and combine results.

---

## 🚀 Best Practices

✔ Choose shard key carefully  
✔ Avoid uneven data distribution  
✔ Monitor shard usage  
✔ Plan for shard rebalancing  
✔ Minimize cross-shard queries  

---

## 🧠 Sharding vs Replication

| Feature | Sharding | Replication |
|--------|----------|-------------|
| Purpose | Scale data storage | Improve availability |
| Data | Split across servers | Copied across servers |
| Writes | Distributed | Usually handled by primary |

Often both techniques are used together.

---

## 🎯 Interview Questions

**Q: What is database sharding?**

Splitting a large database into smaller distributed databases.

---

**Q: Why use sharding?**

To scale databases horizontally and improve performance.

---

**Q: What is a shard key?**

A field used to determine how data is distributed across shards.

---

**Q: Difference between sharding and replication?**

Sharding distributes data, replication copies data.

---

## ✅ Key Takeaway

Database sharding allows systems to handle massive data by distributing it across multiple servers.

It is a critical technique for building **large-scale distributed backend systems**.

✨ End of Day 22