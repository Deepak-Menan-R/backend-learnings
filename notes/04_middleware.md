# Day 04 – Middleware

## 🧠 What is Middleware?

**Middleware** is a layer of logic that sits **between the request and the response**.

It intercepts HTTP requests **before** they reach the route handler  
and/or processes responses **before** they are sent back to the client.

Think of it as:

👉 *"A pipeline of processing steps"*

---

## 🔁 Request Lifecycle with Middleware

Client → Middleware → Route Handler → Middleware → Response

Example flow:

1️⃣ Request received  
2️⃣ Middleware executes  
3️⃣ Request reaches handler  
4️⃣ Response generated  
5️⃣ Middleware processes response  
6️⃣ Response sent  

---

## 🎯 Why Middleware is Important

Middleware is used for:

✔ Authentication  
✔ Authorization  
✔ Logging  
✔ Error handling  
✔ Input validation  
✔ Rate limiting  
✔ Caching  
✔ Request modification  

---

## 🔐 Authentication Middleware Example (Conceptual)

Goal:

Check if user is authenticated **before** accessing protected routes.

Flow:

- Read Authorization header
- Validate token
- Allow / Reject request

---

## 📘 Theoretical Example

Imagine a protected API:

GET /profile


Without middleware:

❌ Every route must manually check authentication

With middleware:

✅ Authentication logic centralized

---

## 🛠 Practical Example (Pseudo Logic)

### Middleware Logic

IF Authorization header missing
RETURN 401 Unauthorized

IF token invalid
RETURN 403 Forbidden

ELSE
Allow request


---

## 🧩 Common Middleware Types

### ✅ Logging Middleware

Logs request details:

- Method
- Endpoint
- Timestamp
- Response time

---

### ✅ Authentication Middleware

Verifies identity.

---

### ✅ Authorization Middleware

Checks permissions/roles.

---

### ✅ Validation Middleware

Validates request body/params.

---

### ✅ Error Handling Middleware

Catches exceptions globally.

---

## ⚙️ Middleware Execution Order (IMPORTANT)

Middleware runs **in the order registered**.

Example:

1️⃣ Logging  
2️⃣ Authentication  
3️⃣ Authorization  
4️⃣ Route handler  

Order mistakes can cause:

❌ Security bugs  
❌ Incorrect responses  

---

## ⚠️ Common Middleware Mistakes

❌ Wrong execution order  
❌ Heavy logic (slow middleware)  
❌ Not calling next handler  
❌ Mixing responsibilities  
❌ Poor error handling  

---

## 🚀 Middleware Best Practices

✔ Keep middleware lightweight  
✔ Single responsibility  
✔ Proper ordering  
✔ Reusable logic  
✔ Clear naming  

---

## 🎯 Interview Questions

**Q: What is middleware?**

A processing layer that intercepts requests/responses.

---

**Q: Why use middleware?**

✔ Centralized logic  
✔ Cleaner routes  
✔ Reusability  
✔ Security  

---

**Q: Examples of middleware usage?**

- Auth
- Logging
- Validation
- Rate limiting

---

**Q: What happens if middleware doesn’t pass request forward?**

Request never reaches handler.

---

## ✅ Key Takeaway

Middleware enables:

✔ Cleaner architecture  
✔ Centralized control  
✔ Reusable backend logic  
✔ Better scalability  