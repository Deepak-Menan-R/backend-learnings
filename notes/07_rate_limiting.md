# Day 07 – Rate Limiting

## 🚦 What is Rate Limiting?

**Rate limiting** is the technique used to control the number of requests  
a client can make to an API within a specific time window.

Goal:

👉 Prevent abuse  
👉 Protect backend resources  
👉 Ensure fair usage  

---

## 🧠 Why Rate Limiting is Important

Without rate limiting:

❌ API abuse  
❌ Server overload  
❌ Denial of Service (DoS) risk  
❌ Unfair usage by aggressive clients  

With rate limiting:

✔ Stability  
✔ Security  
✔ Predictable performance  

---

## 🎯 Common Use Cases

- Prevent brute-force attacks
- Avoid API spamming
- Protect expensive endpoints
- Enforce usage quotas
- Maintain fairness among users

---

## ⏳ Rate Limit Components

A rate limiter typically defines:

- **Limit** → Max requests allowed
- **Time Window** → Duration
- **Client Identifier** → IP / User / API Key / Token

Example:

100 requests per minute per user


---

## 🔁 Example Scenario

Rule:

Limit: 5 requests
Window: 60 seconds


Client behavior:

- First 5 requests → ✅ Allowed
- 6th request → ❌ Blocked

---

## 📦 Response When Limit Exceeded

429 Too Many Requests


Example:

```json
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded. Try again later."
}

🧩 Rate Limiting Strategies
✅ Fixed Window

Requests counted per fixed interval

Simple to implement

Problem:

❌ Burst traffic at window boundary

✅ Sliding Window

More accurate

Prevents burst abuse

✔ Better fairness

✅ Token Bucket

Tokens added at fixed rate

Each request consumes token

✔ Allows controlled bursts

✅ Leaky Bucket

Requests processed at steady rate

Smooth traffic flow

IF request_count > allowed_limit
    RETURN 429 Too Many Requests

ELSE
    Allow request

🔐 Rate Limiting & Security

Helps prevent:

✔ Brute-force attacks
✔ Credential stuffing
✔ API abuse
✔ DoS attempts

⚙️ Where Rate Limiting Can Be Applied

API Gateway

Reverse Proxy

Middleware

Application layer

⚠️ Common Mistakes

❌ No rate limiting on login endpoints
❌ Too strict limits (bad UX)
❌ Too loose limits (ineffective)
❌ Not identifying clients properly
❌ Missing retry headers.

🚀 Best Practices

✔ Use 429 status code
✔ Provide retry information
✔ Different limits per endpoint
✔ Stricter limits for sensitive routes
✔ Use distributed cache (Redis)
✔ Monitor traffic patterns

📬 Helpful Headers

Example:

X-RateLimit-Limit: 100
X-RateLimit-Remaining: 20
X-RateLimit-Reset: 1700000000

