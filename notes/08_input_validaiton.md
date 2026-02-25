# Day 08 – Input Validation

## ✅ What is Input Validation?

**Input validation** is the process of verifying that incoming data  
is **correct, safe, and usable** before processing it.

Goal:

👉 Prevent invalid data  
👉 Protect against security vulnerabilities  
👉 Ensure backend stability  

---

## 🧠 Why Input Validation is Critical

Without validation:

❌ Application crashes  
❌ Corrupted database data  
❌ Security vulnerabilities  
❌ Unexpected behavior  

With validation:

✔ Reliable APIs  
✔ Predictable logic  
✔ Better security  

---

## 🎯 What Should Be Validated?

Validate all external inputs:

- Request body
- Query parameters
- Path variables
- Headers
- File uploads

---

## 📦 Types of Validation

### ✅ Format Validation

Check structure & type.

Examples:

- Email format
- Phone number format
- Date format

---

### ✅ Required Field Validation

Ensure mandatory fields exist.

Example:

❌ Missing `email` → Reject request

---

### ✅ Data Type Validation

Verify correct types.

Examples:

- String
- Integer
- Boolean
- Array

---

### ✅ Range / Constraint Validation

Examples:

- Age ≥ 18
- Password length ≥ 8
- Price > 0

---

### ✅ Business Rule Validation

Examples:

- Username must be unique
- Booking date cannot be past
- Order amount cannot be negative

---

## 🛠 Example Scenario

### ❌ Bad Request (Invalid Input)

**Request**

POST /users
Body:
{
"name": "",
"email": "not-an-email"
}


**Response**
```json
{
  "error": "Validation Error",
  "message": "Invalid email format"
}

✅ Good Request (Valid Input)

Request

POST /users
Body:
{
  "name": "Deepak",
  "email": "deepak@email.com"
}

Response

{
  "id": 1,
  "name": "Deepak",
  "email": "deepak@email.com"
}

🔐 Validation & Security

Input validation protects against:

✔ SQL Injection
✔ XSS (Cross-site scripting)
✔ Command injection
✔ Buffer overflow
✔ Malicious payloads

⚠️ Never Trust Client Input

Golden rule:

👉 All client data is untrusted

Even if frontend validates:

✔ Always validate again in backend

🧩 Common Validation Failures

❌ Missing required fields
❌ Wrong data types
❌ Invalid formats
❌ Constraint violations

📦 Proper Error Response

Use structured validation errors.

Example:

{
  "error": "Validation Error",
  "fields": {
    "email": "Invalid format",
    "password": "Too short"
  }
}

Benefits:

✔ Frontend-friendly
✔ Debug-friendly

⚠️ Common Mistakes

❌ Skipping validation
❌ Validating only on frontend
❌ Poor error messages
❌ Overly strict validation
❌ Inconsistent validation rules

🚀 Best Practices

✔ Validate at API boundary
✔ Clear error messages
✔ Validate types & formats
✔ Enforce constraints
✔ Sanitize inputs
✔ Centralize validation logic

✨ End of Day 08