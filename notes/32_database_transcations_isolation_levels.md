# Day 32 – Database Transactions Isolation Levels

## 🔐 What are Isolation Levels?

**Isolation levels** define how transactions interact with each other in a database system.

They control:

- Visibility of data between transactions
- How concurrent operations behave
- Trade-off between consistency and performance

Goal:

- Maintain data correctness
- Control concurrency issues
- Balance performance vs consistency

---

## 🧠 Why Isolation Levels are Important

In concurrent systems:

- Multiple transactions run at the same time
- They may read/write the same data

Without proper isolation:

❌ Data inconsistency  
❌ Unexpected results  
❌ Race conditions  

With isolation levels:

✔ Controlled concurrency  
✔ Predictable behavior  
✔ Data integrity  

---

## ⚠ Common Concurrency Problems

---

### 1️⃣ Dirty Read

Reading data that is **not yet committed**.

Example:


Transaction A updates balance → Not committed
Transaction B reads that value


If A rolls back:

❌ B has incorrect data

---

### 2️⃣ Non-Repeatable Read

Same query returns **different results** in the same transaction.

Example:


Transaction A reads value = 100
Transaction B updates value to 200
Transaction A reads again → 200


---

### 3️⃣ Phantom Read

New rows appear during a transaction.

Example:


Transaction A: SELECT users WHERE age > 18 → 5 rows
Transaction B inserts new user
Transaction A runs again → 6 rows


---

## 🔁 Isolation Levels (SQL Standard)

---

## 1️⃣ Read Uncommitted

- Lowest isolation level
- Allows dirty reads

### Behavior:

✔ Can read uncommitted data  
✔ Fastest performance  
❌ Least safe  

---

## 2️⃣ Read Committed

- Only reads committed data

### Behavior:

✔ No dirty reads  
❌ Non-repeatable reads possible  
❌ Phantom reads possible  

---

## 3️⃣ Repeatable Read

- Ensures same row values during transaction

### Behavior:

✔ No dirty reads  
✔ No non-repeatable reads  
❌ Phantom reads possible  

---

## 4️⃣ Serializable (Highest Level)

- Full isolation

### Behavior:

✔ No dirty reads  
✔ No non-repeatable reads  
✔ No phantom reads  
❌ Slowest performance  

Transactions behave as if executed sequentially.

---

## 📊 Isolation Levels Comparison

| Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|------|-----------|--------------------|--------------|
| Read Uncommitted | Yes | Yes | Yes |
| Read Committed | No | Yes | Yes |
| Repeatable Read | No | No | Yes |
| Serializable | No | No | No |

---

## 🛠 Example Scenario

Bank account balance:


Transaction A reads balance = 1000
Transaction B updates balance to 500


Isolation level determines:

- Whether A sees updated value
- When A sees updated value

---

## ⚖ Trade-Off

Higher isolation:

✔ More consistency  
❌ Lower performance  

Lower isolation:

✔ Better performance  
❌ More anomalies  

---

## 🚀 When to Use Each Level

### Read Committed

✔ Default in many DBs  
✔ General use cases  

---

### Repeatable Read

✔ Financial data  
✔ Reports  

---

### Serializable

✔ Critical systems (banking)  
✔ Strict correctness needed  

---

## ⚠ Common Mistakes

❌ Always using highest isolation (performance issues)  
❌ Ignoring concurrency problems  
❌ Not understanding trade-offs  

---

## 🎯 Interview Questions

**Q: What are isolation levels?**

Rules that control how transactions interact with each other.

---

**Q: What is a dirty read?**

Reading uncommitted data.

---

**Q: What is phantom read?**

New rows appearing during a transaction.

---

**Q: Which is the strongest isolation level?**

Serializable.

---

## ✅ Key Takeaway

Isolation levels help manage **concurrent transactions safely**.

They ensure:

✔ Data consistency  
✔ Controlled concurrency  
✔ Predictable database behavior  

Choosing the right isolation level is critical for balancing **performance and correctness**.

✨ End of Day 32