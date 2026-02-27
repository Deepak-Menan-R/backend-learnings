# Day 10 – Database Indexing

## 📌 What is Database Indexing?

A **database index** is a data structure that improves the speed of data retrieval  
operations on a database table.

It works like an index in a book:

👉 Instead of scanning every page,  
👉 You jump directly to the required section.

---

## 🧠 Why Indexing is Important

Without indexing:

❌ Full table scan  
❌ Slow queries  
❌ High CPU usage  
❌ Poor scalability  

With indexing:

✔ Faster lookups  
✔ Reduced query time  
✔ Better performance  

---

## 🔍 How Indexing Works (Conceptual)

Imagine a table:

| id | name   | email              |
|----|--------|-------------------|
| 1  | Alice  | alice@email.com   |
| 2  | Bob    | bob@email.com     |
| 3  | Deepak | deepak@email.com  |

If you search:

SELECT * FROM users WHERE email = 'deepak@email.com';


Without index → Database scans every row  
With index → Database jumps directly to matching row  

---

## 🏗 Types of Indexes

### ✅ Primary Index

- Automatically created on primary key
- Unique
- Fast lookups

Example:

PRIMARY KEY (id)


---

### ✅ Unique Index

Ensures uniqueness.

Example:

UNIQUE(email)


Prevents duplicate emails.

---

### ✅ Single-Column Index

Index on one column.

Example:

INDEX(name)


---

### ✅ Composite Index

Index on multiple columns.

Example:

INDEX(first_name, last_name)


Useful when queries filter by both fields.

---

### ✅ Full-Text Index

Used for text search.

Example:

Search blog posts by keywords


---

## ⚡ When to Use Indexes

✔ Frequently searched columns  
✔ Columns used in WHERE  
✔ Columns used in JOIN  
✔ Columns used in ORDER BY  
✔ Columns with high selectivity  

---

## 🚨 When NOT to Use Indexes

❌ Small tables  
❌ Frequently updated columns  
❌ Columns with very few distinct values (e.g., gender)

Too many indexes:

❌ Slower inserts  
❌ Slower updates  
❌ More storage usage  

---

## 🛠 Example Scenario

Query:

SELECT * FROM orders WHERE user_id = 100;


If `user_id` not indexed:

→ Slow for large tables  

If indexed:

→ Fast lookup  

---

## 🧠 What is Selectivity?

**Selectivity** = How unique values are in a column.

High selectivity → Good for indexing  
Low selectivity → Poor candidate  

Example:

- Email → High selectivity ✅  
- Boolean field → Low selectivity ❌  

---

## 🔄 Index Trade-Off

Indexes improve:

✔ Read performance  

But affect:

❌ Write performance  

Every insert/update must update index too.

---

## 📊 Index & Query Optimization

To check performance:

- Use `EXPLAIN` query
- Analyze query plan
- Check if index is used

Example:

EXPLAIN SELECT * FROM users WHERE email = 'a@email.com';


---

## ⚠ Common Indexing Mistakes

❌ Indexing every column  
❌ Ignoring query patterns  
❌ Not monitoring performance  
❌ Wrong column order in composite index  

---

## 🎯 Interview Questions

**Q: What is indexing?**

A data structure that improves query performance.

---

**Q: Why not index everything?**

✔ Slows writes  
✔ Uses memory  
✔ Maintenance overhead  

---

**Q: What is composite index?**

Index on multiple columns.

---

**Q: How to check if index is used?**

Use `EXPLAIN` query.

---

**Q: What is selectivity?**

Measure of uniqueness in a column.

---

## ✅ Key Takeaway

Database indexing:

✔ Improves read performance  
✔ Essential for scalable systems  
✔ Must be used strategically  

✨ End of Day 10