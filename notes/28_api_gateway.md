# Day 28 – API Gateway

## 🌐 What is an API Gateway?

An **API Gateway** is a single entry point for all client requests in a system, especially in **microservices architecture**.

Instead of clients directly calling multiple services, they interact with the API Gateway, which routes requests to the appropriate backend services.

Goal:

- Centralize request handling
- Simplify client interactions
- Improve security and scalability

---

## 🧠 Why API Gateway is Important

Without API Gateway:

❌ Clients must call multiple services  
❌ Complex client logic  
❌ Hard to manage authentication  
❌ Tight coupling between client and services  

With API Gateway:

✔ Single entry point  
✔ Simplified client communication  
✔ Centralized security  
✔ Better monitoring  

---

## 📦 Basic Architecture


Client → API Gateway → Microservices


Example:


Client
|
API Gateway
/ |
User Order Payment
Service Service Service


The gateway routes requests to the correct service.

---

## 🔁 Responsibilities of API Gateway

### 1️⃣ Request Routing

Routes incoming requests to appropriate services.

Example:


/users → User Service
/orders → Order Service


---

### 2️⃣ Authentication & Authorization

Validates user identity and permissions before forwarding requests.

Example:


Authorization: Bearer TOKEN


---

### 3️⃣ Rate Limiting

Controls how many requests a client can make.

---

### 4️⃣ Load Balancing

Distributes requests across multiple service instances.

---

### 5️⃣ Response Aggregation

Combines responses from multiple services into a single response.

Example:


Client requests user dashboard
→ Gateway fetches data from multiple services
→ Combines and returns response


---

### 6️⃣ Caching

Stores frequently accessed responses to improve performance.

---

### 7️⃣ Logging & Monitoring

Tracks requests, errors, and system performance.

---

## 🧩 Example Flow

Client requests user profile:


GET /profile


Flow:


Client → API Gateway → User Service
→ Order Service
→ Notification Service


Gateway aggregates responses and returns:

```json
{
  "user": {...},
  "orders": [...],
  "notifications": [...]
}
🚀 Benefits of API Gateway

✔ Simplifies client interaction
✔ Centralized security
✔ Reduced network calls
✔ Better scalability
✔ Easier monitoring

⚠ Challenges of API Gateway

❌ Single point of failure
❌ Added latency
❌ Complexity in gateway logic

Solution:

✔ Use multiple gateway instances
✔ Load balancing
✔ Failover mechanisms

🛠 Popular API Gateway Tools

Common tools:

AWS API Gateway

Kong

NGINX

Apigee

Zuul (Netflix)

⚠ Common Mistakes

❌ Putting too much logic in gateway
❌ No caching strategy
❌ No rate limiting
❌ Single gateway instance

🎯 Interview Questions

Q: What is an API Gateway?

A single entry point that routes requests to backend services.

Q: Why use API Gateway in microservices?

To simplify client communication and centralize concerns.

Q: What responsibilities does API Gateway handle?

Routing, authentication, rate limiting, caching, and monitoring.

Q: Is API Gateway a single point of failure?

Yes, unless properly replicated and load balanced.

✅ Key Takeaway

API Gateway acts as the front door of a backend system.

It enables:

✔ Simplified architecture
✔ Centralized control
✔ Scalable microservices communication

✨ End of Day 28