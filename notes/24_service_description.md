# Day 24 – Service Discovery

## 🔍 What is Service Discovery?

**Service Discovery** is the mechanism that allows services in a distributed system to **find and communicate with each other dynamically**.

In modern architectures (especially **microservices**), services are deployed on multiple machines and their IP addresses can change frequently.

Service discovery helps services locate each other without hardcoding addresses.

Goal:

- Enable dynamic service communication
- Avoid hardcoded IP addresses
- Improve scalability
- Handle service failures gracefully

---

## 🧠 Why Service Discovery is Important

Without service discovery:

❌ Services must know exact IP addresses of other services  
❌ Hard to scale services dynamically  
❌ Configuration becomes complex  
❌ System becomes fragile  

With service discovery:

✔ Services locate each other automatically  
✔ Dynamic scaling becomes possible  
✔ Infrastructure becomes more flexible  

---

## 📦 Example Problem

Imagine a system with multiple services:

- User Service
- Order Service
- Payment Service

Order Service must communicate with Payment Service.

Without service discovery:


Order Service → http://192.168.1.12:8080


If the Payment Service moves to another server:

❌ Communication breaks.

---

## 🚀 With Service Discovery

Instead of IP addresses:


Order Service → payment-service


The system resolves the service name to the correct instance.

Example flow:


Order Service → Service Registry → Payment Service Instance


---

## 🧩 Components of Service Discovery

### 1️⃣ Service Registry

A central registry that stores information about available services.

Example entries:

| Service Name | Instance Address |
|---------------|------------------|
| payment-service | 10.0.1.12:8080 |
| payment-service | 10.0.1.13:8080 |
| user-service | 10.0.1.20:8080 |

Services register themselves when they start.

---

### 2️⃣ Service Provider

The service that registers itself.

Example:


Payment Service registers itself to registry


---

### 3️⃣ Service Consumer

The service that queries the registry to locate another service.

Example:


Order Service asks registry for Payment Service location


---

## 🔁 Service Discovery Flow

1️⃣ Service starts

2️⃣ Registers with service registry

3️⃣ Another service requests location

4️⃣ Registry returns available instances

5️⃣ Service communicates directly

Example:


Order Service → Registry → Payment Service


---

## 🧠 Client-Side vs Server-Side Discovery

### Client-Side Discovery

Client queries registry and chooses service instance.

Example:


Client → Service Registry → Service Instance


Tools using this pattern:

- Netflix Eureka
- Consul

---

### Server-Side Discovery

Client sends request to load balancer.

Load balancer queries registry and routes request.

Example:


Client → Load Balancer → Service Instance


Used in:

- Kubernetes
- AWS Elastic Load Balancer

---

## 📊 Example with Multiple Instances

Payment service instances:


payment-service-1 → 10.0.0.1
payment-service-2 → 10.0.0.2
payment-service-3 → 10.0.0.3


Order Service requests Payment Service.

Registry returns list of instances.

Client selects one instance.

---

## ⚙ Health Checks

Service registries monitor health of services.

Example health endpoint:


GET /health


If service fails health checks:

❌ Removed from registry.

This prevents traffic from reaching unhealthy services.

---

## 🚀 Popular Service Discovery Tools

Common tools used in modern systems:

- Consul
- Netflix Eureka
- Apache Zookeeper
- etcd
- Kubernetes Service Discovery

---

## ⚠ Common Mistakes

❌ Hardcoding service addresses  
❌ No health checks  
❌ Not removing failed services  
❌ Poor service naming  

---

## 🎯 Interview Questions

**Q: What is service discovery?**

A mechanism that allows services to find and communicate with each other dynamically.

---

**Q: Why is service discovery needed in microservices?**

Because service instances change frequently due to scaling and deployment.

---

**Q: What is a service registry?**

A database of available services and their locations.

---

**Q: Client-side vs server-side discovery?**

Client-side → Client chooses service instance  
Server-side → Load balancer chooses instance

---

## ✅ Key Takeaway

Service discovery enables dynamic communication between services in distributed systems.

It ensures:

✔ Flexible service communication  
✔ Dynamic scaling  
✔ High availability  

Service discovery is a key building block of **microservices architecture**.

✨ End of Day 24