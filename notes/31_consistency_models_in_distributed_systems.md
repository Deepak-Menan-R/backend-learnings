# Day 31 – Consistency Models in Distributed Systems

## 🌐 What are Consistency Models?

**Consistency models** define how and when updates to data become visible across a distributed system.

They describe the **rules of visibility of data** between nodes.

Goal:

- Define how fresh/accurate data is
- Balance consistency vs performance
- Handle distributed data synchronization

---

## 🧠 Why Consistency Models are Important

In distributed systems:

- Data is stored across multiple nodes
- Updates may not reach all nodes instantly

Without defined consistency:

❌ Conflicting data  
❌ Unpredictable behavior  
❌ Poor user experience  

With consistency models:

✔ Controlled data visibility  
✔ Predictable system behavior  
✔ Better system design decisions  

---

## 🔁 Types of Consistency Models

---

## 1️⃣ Strong Consistency

All nodes always return the **latest updated value**.

After a write completes:

✔ Every read gets the updated data  

Example:


User updates profile → All users see updated value immediately


### Characteristics

✔ Most accurate  
❌ Higher latency  
❌ Lower availability during failures  

### Use Cases

- Banking systems  
- Payment systems  
- Critical data systems  

---

## 2️⃣ Eventual Consistency

Data will become consistent **eventually**, but not immediately.

After a write:

✔ Some nodes may still return old data temporarily  

Example:


Social media like count updates after a delay


### Characteristics

✔ High availability  
✔ Better performance  
❌ Temporary inconsistency  

### Use Cases

- Social media  
- Caching systems  
- Distributed databases  

---

## 3️⃣ Read-Your-Writes Consistency

A user always sees their **own updates immediately**.

Example:


User updates profile → Immediately sees updated profile
Other users may still see old data


---

## 4️⃣ Monotonic Reads

Once a user sees a value, they will **never see an older value**.

Example:


User sees version 5 → Will never see version 4 again


---

## 5️⃣ Monotonic Writes

Writes are processed in the **order they were sent**.

Example:


Write1 → Write2 → Write3
System ensures correct order


---

## 6️⃣ Causal Consistency

Operations that are causally related must be seen in order.

Example:


User posts → User edits post
Other users must see post before edit


---

## 📊 Comparison of Models

| Model | Consistency Level | Performance |
|------|------------------|------------|
| Strong | High | Low |
| Eventual | Low | High |
| Read-Your-Writes | Medium | Medium |
| Monotonic Reads | Medium | Medium |
| Causal | Medium-High | Medium |

---

## 🔄 Trade-Offs

Consistency vs Performance:

- Strong consistency → Slower but accurate  
- Eventual consistency → Faster but temporarily inconsistent  

---

## ⚠ Real-World Example

### E-commerce Inventory

- Strong consistency → Prevent overselling  
- Eventual consistency → Faster browsing  

---

### Social Media

- Eventual consistency acceptable  

---

## ⚠ Common Mistakes

❌ Assuming data is always instantly updated  
❌ Ignoring eventual consistency delays  
❌ Using strong consistency everywhere (performance issues)  

---

## 🚀 Best Practices

✔ Choose consistency model based on use case  
✔ Use strong consistency for critical data  
✔ Use eventual consistency for scalability  
✔ Design systems to tolerate delays  

---

## 🎯 Interview Questions

**Q: What is consistency in distributed systems?**

The guarantee of how data updates are visible across nodes.

---

**Q: Strong vs Eventual consistency?**

Strong → Immediate consistency  
Eventual → Delayed consistency  

---

**Q: What is read-your-writes consistency?**

User always sees their own updates.

---

**Q: When to use eventual consistency?**

When high availability and performance are more important than immediate accuracy.

---

## ✅ Key Takeaway

Consistency models define how distributed systems manage data visibility.

Choosing the right model is critical for:

✔ Performance  
✔ Scalability  
✔ User experience  

✨ End of Day 31