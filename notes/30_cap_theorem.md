# Day 30 – CAP Theorem

## ⚖️ What is CAP Theorem?

The **CAP Theorem** states that a distributed system can only guarantee **two out of three** properties:

- **C → Consistency**
- **A → Availability**
- **P → Partition Tolerance**

👉 It is impossible to achieve all three simultaneously in a distributed system.

---

## 🧠 Why CAP Theorem is Important

In distributed systems:

- Network failures are inevitable
- Systems must make trade-offs

CAP helps architects decide:

✔ How system behaves under failure  
✔ What to prioritize  
✔ How to design scalable systems  

---

## 📦 The Three Properties Explained

### 1️⃣ Consistency (C)

All nodes see the **same data at the same time**.

Example:


User updates profile → All users immediately see updated data


✔ Strong consistency  
❌ May reduce availability  

---

### 2️⃣ Availability (A)

Every request receives a **response**, even if data is not fully up-to-date.

Example:


System always responds, but data may be slightly outdated


✔ High uptime  
❌ Possible stale data  

---

### 3️⃣ Partition Tolerance (P)

System continues to operate despite **network failures (partitions)**.

Example:


Server A cannot communicate with Server B, but system still runs


✔ Essential for distributed systems  

---

## 🔁 CAP Trade-Offs

Since partition tolerance is **mandatory** in distributed systems,  
the real trade-off is between:

👉 Consistency vs Availability

---

## 🧩 CAP Combinations

### ✅ CP (Consistency + Partition Tolerance)

- Always returns consistent data
- May reject requests during failures

Example systems:

- HBase
- MongoDB (in certain modes)

Use cases:

✔ Banking systems  
✔ Financial transactions  

---

### ✅ AP (Availability + Partition Tolerance)

- Always responds to requests
- Data may be temporarily inconsistent

Example systems:

- Cassandra
- DynamoDB

Use cases:

✔ Social media  
✔ Real-time analytics  

---

### ❌ CA (Consistency + Availability)

- Possible only when no partitions exist
- Not realistic in distributed systems

---

## 📊 Visual Understanding

    Consistency (C)
       /     \
      /       \
   CA         CP
    \         /
     \       /
  Availability (A)
         |
 Partition Tolerance (P)

---

## 🔄 Real-World Examples

### Banking System (CP)

- Accuracy is critical
- Cannot allow inconsistent balance

---

### Social Media Feed (AP)

- Slight delay acceptable
- Always respond quickly

---

## ⚠ Network Partition Example


Server A ←X→ Server B


Network failure occurs.

System must choose:

- Stop serving requests → Maintain consistency  
- Continue serving → Lose consistency temporarily  

---

## 🚀 Key Design Decision

Ask:

👉 Is consistency more important?  
👉 Or availability more important?

Then design system accordingly.

---

## ⚠ Common Misunderstandings

❌ CAP is not about normal operation  
✔ It applies during network failures  

❌ You can achieve all three  
✔ You must choose trade-offs  

---

## 🎯 Interview Questions

**Q: What is CAP theorem?**

A distributed system can only guarantee two of Consistency, Availability, and Partition Tolerance.

---

**Q: Why is partition tolerance mandatory?**

Because network failures are unavoidable.

---

**Q: CP vs AP systems?**

CP → Consistent but may reject requests  
AP → Available but may return stale data  

---

**Q: Example of CP system?**

Banking systems.

---

**Q: Example of AP system?**

Social media platforms.

---

## ✅ Key Takeaway

CAP theorem highlights the **trade-offs** in distributed system design.

You must choose between:

✔ Strong consistency  
✔ High availability  

while always handling network partitions.

✨ End of Day 30