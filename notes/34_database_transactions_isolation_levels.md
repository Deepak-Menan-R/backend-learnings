# Day 34 – Database Transactions Isolation Levels

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

- Multiple transactions run simultaneously  
- They may read/write the same data  

Without isolation:

❌ Data inconsistency  
❌ Race conditions  
❌ Unpredictable results  

With isolation:

✔ Controlled concurrency  
✔ Data integrity  
✔ Predictable behavior  

---

## ⚠ Common Concurrency Problems

### 1️⃣ Dirty Read

Reading **uncommitted data** from another transaction.

Example:


Transaction A updates balance → Not committed
Transaction B reads that value


If A rolls back:

❌ B has invalid data  

---

### 2️⃣ Non-Repeatable Read

Same query returns different results in one transaction.

Example:


Transaction A reads value = 100
Transaction B updates value to 200
Transaction A reads again → 200


---

### 3️⃣ Phantom Read

New rows appear during a transaction.

Example:


Transaction A: SELECT users WHERE age > 18 → 5 rows
Transaction B inserts new row
Transaction A runs again → 6 rows


---

## 🔁 Isolation Levels (SQL Standard)

---

## 1️⃣ Read Uncommitted

- Lowest isolation level  
- Allows dirty reads  

✔ Fastest  
❌ Unsafe  

---

## 2️⃣ Read Committed

- Reads only committed data  

✔ No dirty reads  
❌ Non-repeatable reads possible  
❌ Phantom reads possible  

---

## 3️⃣ Repeatable Read

- Ensures same row values during transaction  

✔ No dirty reads  
✔ No non-repeatable reads  
❌ Phantom reads possible  

---

## 4️⃣ Serializable (Highest Level)

- Complete isolation  

✔ No dirty reads  
✔ No non-repeatable reads  
✔ No phantom reads  
❌ Slowest  

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

Bank account example:


Transaction A reads balance = 1000
Transaction B updates balance to 500


Isolation level determines:

- When A sees the update  
- Whether A sees consistent data  

---

## ⚖ Trade-Off

Higher isolation:

✔ Strong consistency  
❌ Lower performance  

Lower isolation:

✔ Better performance  
❌ More anomalies  

---

## 🚀 When to Use Each Level

### Read Committed

✔ Default in most systems  
✔ Suitable for general applications  

---

### Repeatable Read

✔ Reporting systems  
✔ Financial reads  

---

### Serializable

✔ Banking systems  
✔ Critical operations  

---

## ⚠ Common Mistakes

❌ Always using highest isolation level  
❌ Ignoring performance impact  
❌ Not understanding concurrency issues  

---

## 🎯 Interview Questions

**Q: What are isolation levels?**

Rules that control how transactions interact in a database.

---

**Q: What is a dirty read?**

Reading uncommitted data.

---

**Q: What is phantom read?**

New rows appearing during a transaction.

---

**Q: Which is strongest isolation level?**

Serializable.

---

## ✅ Key Takeaway

Isolation levels help manage concurrent transactions safely.

They balance:

✔ Data consistency  
✔ Performance  

Choosing the right level is critical for building reliable backend systems.

✨ End of Day 34