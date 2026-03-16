# Day 27 – API Rate Limiting Algorithms

## 🚦 What is Rate Limiting?

**Rate limiting** is the technique used to control how many requests a client can send to an API within a specified time period.

It protects systems from:

- Abuse
- Overload
- Brute-force attacks
- Resource exhaustion

Example rule:


100 requests per minute per user


---

## 🧠 Why Rate Limiting is Important

Without rate limiting:

❌ APIs can be overwhelmed  
❌ System resources can be exhausted  
❌ Malicious users can abuse services  

With rate limiting:

✔ Protect backend services  
✔ Ensure fair usage  
✔ Maintain system stability  
✔ Prevent denial-of-service attacks  

---

## 📦 Common Rate Limiting Algorithms

Several algorithms are used to implement rate limiting.

---

## 1️⃣ Fixed Window Algorithm

The **Fixed Window** algorithm limits requests within a fixed time window.

Example:


Limit: 100 requests per minute


Flow:


00:00 - 00:59 → Allow up to 100 requests
01:00 - 01:59 → Counter resets


### Example


Request 1 → Allowed
Request 100 → Allowed
Request 101 → Rejected


### Advantages

✔ Simple implementation  
✔ Easy to understand  

### Disadvantages

❌ Burst traffic problem near window boundaries

Example:


100 requests at 00:59
100 requests at 01:00


200 requests in a few seconds.

---

## 2️⃣ Sliding Window Algorithm

Sliding window improves the fixed window approach.

Instead of fixed intervals, it considers requests in a **rolling time window**.

Example:


100 requests allowed in the last 60 seconds


Each request checks the last 60 seconds of activity.

### Advantages

✔ More accurate rate limiting  
✔ Prevents burst spikes  

### Disadvantages

❌ Slightly more complex implementation  

---

## 3️⃣ Token Bucket Algorithm

The **Token Bucket** algorithm controls request flow using tokens.

Mechanism:

- A bucket contains tokens
- Each request consumes one token
- Tokens refill over time

Example:


Bucket size = 10 tokens
Refill rate = 1 token per second


If bucket is empty:

❌ Request rejected.

### Advantages

✔ Allows controlled bursts  
✔ Efficient for distributed systems  

---

## 4️⃣ Leaky Bucket Algorithm

The **Leaky Bucket** algorithm processes requests at a constant rate.

Mechanism:

- Requests enter bucket
- Requests leave bucket at fixed rate

Example:


Processing rate = 5 requests per second


Extra requests are queued or dropped.

### Advantages

✔ Smooth request processing  
✔ Prevents sudden spikes  

---

## 📊 Comparison of Algorithms

| Algorithm | Burst Handling | Complexity |
|----------|---------------|-----------|
| Fixed Window | Poor | Simple |
| Sliding Window | Good | Medium |
| Token Bucket | Excellent | Medium |
| Leaky Bucket | Good | Medium |

---

## ⚙ Rate Limit Response

When rate limit exceeded:


429 Too Many Requests


Example response:

```json
{
  "error": "Too Many Requests",
  "message": "Rate limit exceeded"
}
📬 Useful Rate Limit Headers

APIs often return headers to inform clients about limits.

Example:

X-RateLimit-Limit: 100
X-RateLimit-Remaining: 20
X-RateLimit-Reset: 1712345678

These headers help clients manage request rates.

🚀 Real-World Tools for Rate Limiting

Popular tools include:

NGINX rate limiting

Envoy proxy

Kong API Gateway

AWS API Gateway

These systems implement rate limiting efficiently.

⚠ Common Mistakes

❌ No rate limiting on login endpoints
❌ Too strict limits blocking legitimate users
❌ No retry guidance
❌ Not using distributed rate limiting

🎯 Interview Questions

Q: What is rate limiting?

Limiting how many requests a client can send within a time period.

Q: Which status code is used for rate limit violations?

429 Too Many Requests

Q: Difference between token bucket and leaky bucket?

Token bucket allows bursts, while leaky bucket processes requests at a fixed rate.

Q: Why use sliding window instead of fixed window?

Sliding window prevents burst traffic at window boundaries.

✅ Key Takeaway

Rate limiting protects backend systems from overload and abuse.

Understanding different algorithms helps design scalable and resilient APIs.

✨ End of Day 27