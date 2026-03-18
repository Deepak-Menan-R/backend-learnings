# Day 29 – Database Normalization

## 🗄 What is Database Normalization?

**Database normalization** is the process of organizing data in a database  
to reduce redundancy and improve data integrity.

It involves dividing large tables into smaller related tables  
and defining relationships between them.

Goal:

- Eliminate duplicate data
- Ensure data consistency
- Improve database design
- Avoid anomalies

---

## 🧠 Why Normalization is Important

Without normalization:

❌ Data duplication  
❌ Inconsistent data  
❌ Difficult updates  
❌ Data anomalies  

With normalization:

✔ Clean database design  
✔ Reduced redundancy  
✔ Improved consistency  
✔ Easier maintenance  

---

## 📦 Example Problem (Unnormalized Table)

| user_id | name   | order_id | product   |
|--------|--------|----------|-----------|
| 1      | Alice  | 101      | Laptop    |
| 1      | Alice  | 102      | Phone     |

Problems:

❌ Duplicate user data  
❌ Wasted storage  
❌ Update issues  

---

## 🔁 What are Normal Forms?

Normalization is done in steps called **Normal Forms (NF)**.

---

## 1️⃣ First Normal Form (1NF)

### Rule:
- No repeating groups
- Each column must contain atomic (indivisible) values

❌ Bad:

| user_id | products        |
|--------|----------------|
| 1      | Laptop, Phone  |

✔ Good:

| user_id | product |
|--------|--------|
| 1      | Laptop |
| 1      | Phone  |

---

## 2️⃣ Second Normal Form (2NF)

### Rule:
- Must be in 1NF
- No partial dependency on composite key

Example problem:

| user_id | order_id | user_name |
|--------|----------|-----------|

Here:

- `user_name` depends only on `user_id`, not full key

✔ Solution:

Split into:

**Users Table**

| user_id | name  |
|--------|------|
| 1      | Alice |

**Orders Table**

| order_id | user_id |
|----------|--------|
| 101      | 1      |

---

## 3️⃣ Third Normal Form (3NF)

### Rule:
- Must be in 2NF
- No transitive dependency

Example:

| user_id | user_name | city_name | city_zip |
|--------|----------|-----------|----------|

Here:

- `city_zip` depends on `city_name`, not directly on `user_id`

✔ Solution:

Split into:

**Users Table**

| user_id | user_name | city_name |
|--------|----------|-----------|

**Cities Table**

| city_name | city_zip |
|-----------|----------|

---

## ⚠ Types of Anomalies

### 1️⃣ Insertion Anomaly

Cannot insert data without other unrelated data.

---

### 2️⃣ Update Anomaly

Updating data in one place but not others leads to inconsistency.

---

### 3️⃣ Deletion Anomaly

Deleting a record removes unintended data.

---

## ⚖ Normalization vs Denormalization

| Feature | Normalization | Denormalization |
|--------|--------------|----------------|
| Data Redundancy | Low | High |
| Read Performance | Slower | Faster |
| Write Performance | Faster | Slower |
| Complexity | Higher | Lower |

---

## 🚀 When to Use Normalization

✔ OLTP systems (transactional systems)  
✔ Data consistency is critical  
✔ Frequent updates  

---

## 🚀 When to Use Denormalization

✔ Read-heavy systems  
✔ Analytics systems  
✔ Performance optimization  

---

## ⚠ Common Mistakes

❌ Over-normalization (too many joins)  
❌ Ignoring performance trade-offs  
❌ Not considering use case  

---

## 🎯 Interview Questions

**Q: What is normalization?**

Organizing data to reduce redundancy and improve integrity.

---

**Q: What is 1NF?**

No repeating groups, atomic values.

---

**Q: What is 2NF?**

No partial dependency on composite keys.

---

**Q: What is 3NF?**

No transitive dependency.

---

**Q: Difference between normalization and denormalization?**

Normalization reduces redundancy, denormalization improves read performance.

---

## ✅ Key Takeaway

Database normalization ensures:

✔ Clean structure  
✔ Data consistency  
✔ Reduced redundancy  

It is essential for designing efficient and reliable databases.

✨ End of Day 29