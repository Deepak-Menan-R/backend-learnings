# Day 03 – Authentication & Authorization

## 🔐 What is Authentication?

**Authentication** is the process of verifying **who the user is**.

It answers the question:

👉 *"Are you really who you claim to be?"*

Examples:

- Username & Password
- OTP
- Biometric login
- API Keys
- Tokens

---

## ✅ What is Authorization?

**Authorization** determines **what an authenticated user is allowed to do**.

It answers:

👉 *"What actions/resources can you access?"*

Examples:

- Admin vs User permissions
- Read vs Write access
- Role-based access

---

## 🎯 Key Difference (Very Common Interview Question)

| Concept | Purpose |
|---------|----------|
| Authentication | Verify identity |
| Authorization | Verify permissions |

---

## 🔑 Common Authentication Methods

### 1️⃣ Username & Password

Traditional method.

Flow:

1. User submits credentials  
2. Server validates  
3. Access granted/denied  

---

### 2️⃣ Session-Based Authentication

After login:

- Server creates session
- Session ID stored in cookie
- Cookie sent automatically

**Pros**
- Simple
- Good for traditional web apps

**Cons**
- Harder to scale (stateful)

---

### 3️⃣ Token-Based Authentication (Modern Standard)

Server issues token after login.

Client sends token with each request.

Example:

Authorization: Bearer TOKEN


**Pros**
- Stateless
- Scalable
- Ideal for APIs & microservices

---

## 🎟 JSON Web Token (JWT)

Very popular token format.

Structure:

HEADER.PAYLOAD.SIGNATURE

Example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...


---

## 🧠 JWT Components

### Header
Contains algorithm & token type.

Example:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload

Contains claims (data).

Example:

{
  "user_id": 123,
  "role": "admin"
}

Signature

Ensures token integrity.

🔁 Authentication Flow (Token-Based)

1️⃣ Client logs in
2️⃣ Server validates credentials
3️⃣ Server generates token
4️⃣ Client stores token
5️⃣ Client sends token in headers

🛡 Authorization Strategies
✅ Role-Based Access Control (RBAC)

Access based on roles.

Examples:

Admin → Full access

User → Limited access

✅ Permission-Based Access

Granular control.

Examples:

CanEditUsers

CanDeleteOrders

⚠️ Common Security Mistakes

❌ Storing passwords in plain text
❌ Not hashing passwords
❌ Weak tokens
❌ Long-lived tokens without expiry
❌ Missing authorization checks

🔒 Password Best Practices

✔ Hash passwords (bcrypt, argon2)
✔ Never store raw passwords
✔ Use salt
✔ Enforce strong password rules

⏳ Token Best Practices

✔ Set expiration (exp)
✔ Use refresh tokens
✔ Secure storage
✔ HTTPS only

