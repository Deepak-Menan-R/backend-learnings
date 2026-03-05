# Day 16 – API Pagination

## 📄 What is Pagination?

**Pagination** is the technique of dividing large datasets into smaller chunks (pages) so that clients can retrieve data in manageable portions instead of loading everything at once.

Instead of returning thousands of records in one response, the API returns a limited subset of results.

Goal:

- Improve performance
- Reduce response size
- Provide better user experience
- Reduce server load

---

## 🧠 Why Pagination is Important

Without pagination:

❌ Large responses  
❌ Slow API performance  
❌ High memory usage  
❌ Increased network bandwidth  

With pagination:

✔ Faster responses  
✔ Efficient data transfer  
✔ Better scalability  
✔ Controlled data access  

---

## 📦 Example Problem

Suppose a database has **1,000,000 users**.

API:

```
GET /users
```

If the API returns all users:

❌ Very large response  
❌ High server load  

Instead use pagination:

```
GET /users?page=1&limit=10
```

This returns only **10 users per request**.

---

## 📊 Basic Pagination Parameters

| Parameter | Description |
|----------|-------------|
| page | Page number |
| limit | Number of items per page |
| offset | Starting index |
| cursor | Position reference for next data |

---

## 🧩 Pagination Strategies

### 1️⃣ Offset-Based Pagination

Most common method.

Example:

```
GET /users?offset=20&limit=10
```

Meaning:

- Skip first 20 records
- Return next 10 records

---

### 2️⃣ Page-Based Pagination

Uses page numbers.

Example:

```
GET /users?page=2&limit=10
```

Meaning:

- Page 2
- 10 records per page

---

### 3️⃣ Cursor-Based Pagination (Advanced)

Uses a cursor pointing to last retrieved item.

Example:

```
GET /users?cursor=eyJpZCI6MTAwfQ
```

Benefits:

✔ Efficient for large datasets  
✔ Avoids offset scanning  

Used by:

- Twitter
- Facebook
- Instagram APIs

---

## 📬 Example Response with Pagination

```json
{
  "page": 1,
  "limit": 10,
  "total": 120,
  "data": [
    { "id": 1, "name": "Alice" },
    { "id": 2, "name": "Bob" }
  ]
}

## 📊 Useful Pagination Metadata

APIs often return additional metadata:

```json
{
  "page": 1,
  "limit": 10,
  "total_pages": 12,
  "total_items": 120
}
```

This helps clients navigate pages.

## 🧠 Pagination Query Example

Example request:

```
GET /products?page=3&limit=20
```

Meaning:

Third page

20 items per page

## ⚠ Offset Pagination Performance Issue

For very large tables:

```sql
SELECT * FROM users LIMIT 10 OFFSET 1000000
```

Problem:

❌ Database scans large number of rows.

Solution:

✔ Cursor-based pagination.

## 🚀 Pagination Best Practices

✔ Always limit response size
✔ Provide pagination metadata
✔ Use sensible default limits
✔ Prevent extremely large limits
✔ Use cursor pagination for large datasets

Example limit restriction:

```python
max_limit = 100
```

✅ Key Takeaway

Pagination is essential for building scalable APIs.

It ensures:

✔ Efficient data transfer
✔ Faster responses
✔ Better user experience

✨ End of Day 16