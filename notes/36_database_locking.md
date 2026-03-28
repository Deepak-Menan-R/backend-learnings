# Day 36 – Database Locking (Pessimistic vs Optimistic Locking)

## 🔐 What is Database Locking?

**Database locking** is a mechanism used to control access to data when multiple transactions try to read/write the same resource simultaneously.

It ensures:

- Data consistency  
- Prevents conflicts  
- Safe concurrent operations  

---

## 🧠 Why Locking is Important

In concurrent systems:

- Multiple users may update the same data
- Without locking → conflicts occur

Example:


User A updates balance
User B updates balance at same time


Without locking:

❌ Data inconsistency  
❌ Lost updates  

With locking:

✔ Safe updates  
✔ Controlled access  

---

## 🔁 Types of Locking

There are two major approaches:

👉 **Pessimistic Locking**  
👉 **Optimistic Locking**

---

## 🧩 1️⃣ Pessimistic Locking

### 📌 Concept

Assumes conflicts **will happen**, so it locks the data immediately.

Once a transaction locks a row:

✔ No other transaction can modify it  

---

### ⚙ Example


Transaction A locks row
Transaction B tries to update → must wait


---

### 📦 SQL Example


SELECT * FROM users WHERE id = 1 FOR UPDATE;


This locks the row until transaction completes.

---

### ✅ Advantages

✔ Strong consistency  
✔ Prevents conflicts completely  

---

### ❌ Disadvantages

❌ Reduced concurrency  
❌ Possible deadlocks  
❌ Slower performance  

---

## 🧩 2️⃣ Optimistic Locking

### 📌 Concept

Assumes conflicts are **rare**.

Instead of locking:

✔ Check if data was modified before updating  

---

### ⚙ How it Works

- Each row has a version/timestamp
- Before update → check version
- If changed → reject update

---

### 📦 Example

Initial state:


balance = 1000, version = 1


Transaction A updates:


balance = 900, version = 2


Transaction B tries update with old version:

❌ Update fails  

---

### ✅ Advantages

✔ Better performance  
✔ Higher concurrency  
✔ No locks required  

---

### ❌ Disadvantages

❌ Retry logic required  
❌ Possible update failures  

---

## 📊 Pessimistic vs Optimistic Locking

| Feature | Pessimistic | Optimistic |
|--------|-------------|------------|
| Approach | Lock first | Check before update |
| Performance | Lower | Higher |
| Concurrency | Low | High |
| Deadlocks | Possible | No |
| Use Case | High conflict systems | Low conflict systems |

---

## ⚠ Deadlocks (Important Concept)

A **deadlock** occurs when two transactions wait for each other.

Example:


Transaction A locks Row1 → waits for Row2
Transaction B locks Row2 → waits for Row1


Result:

❌ Both stuck  

---

## 🛠 Example Use Cases

### Pessimistic Locking

✔ Banking systems  
✔ Inventory management  
✔ High conflict scenarios  

---

### Optimistic Locking

✔ Web applications  
✔ Low contention systems  
✔ High read traffic  

---

## 🚀 Best Practices

✔ Use optimistic locking when conflicts are rare  
✔ Use pessimistic locking for critical operations  
✔ Avoid long transactions  
✔ Monitor deadlocks  

---

## 🎯 Interview Questions

**Q: What is database locking?**

A mechanism to control concurrent access to data.

---

**Q: Pessimistic vs Optimistic locking?**

Pessimistic → Lock data early  
Optimistic → Check for conflicts before update  

---

**Q: What is a deadlock?**

Two transactions waiting on each other indefinitely.

---

**Q: When to use optimistic locking?**

When conflicts are rare and performance is important.

---

## ✅ Key Takeaway

Database locking ensures safe concurrent operations.

- Pessimistic → Safe but slower  
- Optimistic → Fast but needs validation  

Choosing the right approach depends on **system requirements and contention level**.

✨ End of Day 36