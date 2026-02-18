# Day 01 – REST API Design Principles

## 🌐 What is REST?

**REST (Representational State Transfer)** is an architectural style for designing networked applications.  
It defines a set of constraints used to create scalable, simple, and stateless web services.

REST is **not a protocol**, but a **design philosophy** typically implemented using HTTP.

---

## 🧠 Core REST Principles (VERY IMPORTANT)

### 1️⃣ **Client–Server Architecture**

Separation of concerns:

• Client → Handles UI / User Interaction  
• Server → Handles Logic / Data / Processing  

✅ Improves scalability  
✅ Allows independent evolution  

---

### 2️⃣ **Statelessness**

Each request must contain **all necessary information**.

Server does **NOT** store client session state between requests.

✅ Easier scaling  
✅ Better reliability  
✅ Simpler architecture  

Example:

✔ Good → Request includes auth token  
❌ Bad → Server remembers user session internally  

---

### 3️⃣ **Resource-Based Design**

Everything is treated as a **resource**.

Examples:

• User  
• Product  
• Order  
• Payment  

Each resource is identified via **URI (endpoint)**.

Example:

/users
/users/123
/orders/456

---

### 4️⃣ **Uniform Interface**

Consistent interaction rules:

• Standard HTTP methods  
• Predictable URLs  
• Standard status codes  
• Structured responses (usually JSON)

---

### 5️⃣ **HTTP Methods (CRITICAL FOR INTERVIEWS)**

| Method | Purpose | Idempotent? |
|--------|---------|-------------|
| GET    | Retrieve resource | ✅ Yes |
| POST   | Create resource | ❌ No |
| PUT    | Update/Replace resource | ✅ Yes |
| PATCH  | Partial update | ❌ Usually No |
| DELETE | Remove resource | ✅ Yes |

---

## 🔁 Idempotency (Common Interview Question)

**Idempotent → Multiple identical requests produce same result**

Examples:

✔ PUT /users/123 → same update each time  
✔ DELETE /users/123 → deleting again changes nothing  

❌ POST → Creates new resource every time  

---

## 📦 HTTP Status Codes (Know These Well)

| Code | Meaning |
|------|---------|
| 200  | OK |
| 201  | Created |
| 204  | No Content |
| 400  | Bad Request |
| 401  | Unauthorized |
| 403  | Forbidden |
| 404  | Not Found |
| 500  | Server Error |

---

## 🧭 Good REST URL Design

### ✅ Use nouns, NOT verbs

✔ `/users`  
❌ `/getUsers`

✔ `/orders/123`  
❌ `/fetchOrder`

---

### ✅ Use hierarchy for relationships

✔ `/users/123/orders`  
✔ `/orders/456/items`

---

### ✅ Use query parameters for filtering

✔ `/products?category=electronics&sort=price`

---

## 📘 Theoretical Example

Imagine designing an API for a **Library System**.

### Resources:

• Books  
• Members  
• Loans  

### Endpoints:

GET `/books` → List all books  
GET `/books/10` → Get book with ID 10  
POST `/books` → Add new book  
PUT `/books/10` → Replace book details  
DELETE `/books/10` → Remove book  

---

## 🛠 Practical Example (Backend Thinking)

Let’s design a **User Management API**.

---
```json
✅ Retrieve Users

Request

GET /users

Response

200 OK
[
  { "id": 1, "name": "Alice" },
  { "id": 2, "name": "Bob" }
]

✅ Create User

Request

POST /users
Body:
{
  "name": "Charlie"
}

Response

201 Created
{
  "id": 3,
  "name": "Charlie"
}

✅ Update User

Request

PUT /users/3
Body:
{
  "name": "Charlie Updated"
}

Response

200 OK
{
  "id": 3,
  "name": "Charlie Updated"
}

✅ Delete User

Request

DELETE /users/3


Response

204 No Content

