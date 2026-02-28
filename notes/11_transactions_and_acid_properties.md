# Day 11 – Transactions & ACID Properties

## 🔄 What is a Transaction?

A **transaction** is a sequence of one or more database operations  
executed as a single logical unit of work.

A transaction ensures:

👉 Either all operations succeed  
👉 Or none of them are applied  

This guarantees data consistency.

---

## 🧠 Why Transactions Are Important

Without transactions:

❌ Partial updates  
❌ Inconsistent data  
❌ Corrupted state  
❌ Financial/accounting errors  

With transactions:

✔ Data integrity  
✔ Consistency  
✔ Reliability  

---

## 📦 Real-World Example

Imagine transferring ₹100 from Account A to Account B.

Steps:

1️⃣ Deduct ₹100 from A  
2️⃣ Add ₹100 to B  

If step 1 succeeds but step 2 fails:

❌ Money lost  

Using a transaction:

✔ Either both succeed  
✔ Or both rollback  

---

## 🔐 ACID Properties (VERY IMPORTANT FOR INTERVIEWS)

Transactions follow **ACID**:

| Property | Meaning |
|----------|----------|
| A | Atomicity |
| C | Consistency |
| I | Isolation |
| D | Durability |

---

## 🧩 Atomicity

**All or nothing.**

If any part fails → Entire transaction rolls back.

Example:

- Deduct + Add
- If Add fails → Deduct also undone

---

## 🧩 Consistency

Transaction moves database from one valid state to another.

Constraints always preserved:

✔ Unique keys  
✔ Foreign keys  
✔ Data types  

---

## 🧩 Isolation

Multiple transactions do not interfere incorrectly.

Even if running concurrently:

✔ Data remains consistent  

Isolation levels control this behavior.

---

## 🧩 Durability

Once committed:

✔ Data is permanently stored  
✔ Survives crashes  

---

## 🔁 Transaction Lifecycle

1️⃣ BEGIN  
2️⃣ Execute queries  
3️⃣ COMMIT (success)  
OR  
4️⃣ ROLLBACK (failure)

Example:

BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;


---

## ⚠ If Error Occurs

ROLLBACK;


All changes undone.

---

## 🧠 Isolation Levels (Advanced Concept)

Isolation determines how transactions see each other.

| Level | Behavior |
|-------|----------|
| Read Uncommitted | Can read uncommitted data |
| Read Committed | Can read committed data only |
| Repeatable Read | Same row read gives same result |
| Serializable | Strictest level |

---

## ⚠ Common Concurrency Problems

### ❌ Dirty Read
Reading uncommitted data.

### ❌ Non-Repeatable Read
Same query returns different results in same transaction.

### ❌ Phantom Read
New rows appear between reads.

---

## 🛠 When to Use Transactions

✔ Financial operations  
✔ Inventory updates  
✔ Multi-table updates  
✔ Critical business logic  

---

## 🚫 When Not Necessary

❌ Simple read-only queries  
❌ Non-critical operations  

Overusing transactions can reduce performance.

---

## 🚀 Best Practices

✔ Keep transactions short  
✔ Avoid long locks  
✔ Handle exceptions properly  
✔ Always commit or rollback  
✔ Use proper isolation level  

---

## 🎯 Interview Questions

**Q: What is a transaction?**

A group of operations executed as a single unit.

---

**Q: What is ACID?**

Atomicity, Consistency, Isolation, Durability.

---

**Q: What happens if transaction fails?**

Rollback.

---

**Q: What is dirty read?**

Reading uncommitted data.

---

**Q: Why keep transactions short?**

To reduce locks and improve performance.

---

## ✅ Key Takeaway

Transactions ensure:

✔ Data integrity  
✔ Reliability  
✔ Safe concurrent operations  

ACID guarantees correctness in database systems.

✨ End of Day 11