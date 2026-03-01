# Day 12 – System Design Basics for Backend Engineers

## 🏗 What is System Design?

**System design** is the process of defining the architecture, components,  
modules, interfaces, and data flow of a system to meet specific requirements.

For backend engineers, it focuses on:

👉 Scalability  
👉 Reliability  
👉 Performance  
👉 Maintainability  

---

## 🎯 Why System Design Matters

As applications grow:

❌ More users  
❌ More data  
❌ More traffic  
❌ More complexity  

Good system design ensures:

✔ High availability  
✔ Fault tolerance  
✔ Efficient scaling  
✔ Clean architecture  

---

## 🧠 High-Level Design (HLD) vs Low-Level Design (LLD)

### ✅ High-Level Design (HLD)

Describes:

- System architecture
- Components
- Data flow
- External integrations

Example:

Client → Load Balancer → App Servers → Database → Cache

---

### ✅ Low-Level Design (LLD)

Describes:

- Classes
- Modules
- APIs
- Database schema
- Logic implementation

---

## 🧩 Core System Design Components

### 1️⃣ Client

- Web app
- Mobile app
- External services

---

### 2️⃣ Load Balancer

Distributes traffic across servers.

Benefits:

✔ Prevent overload  
✔ Improve availability  
✔ Enable horizontal scaling  

---

### 3️⃣ Application Servers

Handle:

- Business logic
- API processing
- Authentication
- Validation

---

### 4️⃣ Database

Stores persistent data.

Types:

- Relational (SQL)
- NoSQL

---

### 5️⃣ Cache

Improves performance by storing frequently accessed data.

Example:

- Redis
- In-memory cache

---

## ⚖ Horizontal vs Vertical Scaling

### ✅ Vertical Scaling

Increase power of single machine.

- More RAM
- More CPU

Limitations:

❌ Hardware limits  
❌ Expensive  

---

### ✅ Horizontal Scaling

Add more machines.

✔ Better scalability  
✔ Fault tolerance  
✔ Industry standard  

---

## 🔄 Monolith vs Microservices

### 🧱 Monolith

Single codebase.

Pros:

✔ Simple  
✔ Easy to deploy  

Cons:

❌ Hard to scale independently  
❌ Large codebase  

---

### 🧩 Microservices

Multiple independent services.

Pros:

✔ Independent scaling  
✔ Better modularity  

Cons:

❌ Complex communication  
❌ Operational overhead  

---

## 📊 CAP Theorem (Advanced Concept)

A distributed system can only guarantee **two** of the following:

| Letter | Meaning |
|--------|----------|
| C | Consistency |
| A | Availability |
| P | Partition Tolerance |

In distributed systems:

👉 Partition tolerance is mandatory  
So trade-off is between Consistency & Availability.

---

## ⚠ Single Point of Failure (SPOF)

A component whose failure causes system failure.

Examples:

❌ Single database  
❌ Single server  

Solution:

✔ Replication  
✔ Load balancing  
✔ Redundancy  

---

## 📦 Example System – URL Shortener (Conceptual)

Components:

1️⃣ Client  
2️⃣ API Server  
3️⃣ Database  
4️⃣ Cache  

Flow:

User → Shorten URL → Store mapping → Return short link  

Optimizations:

✔ Cache popular links  
✔ Use hashing for IDs  
✔ Add rate limiting  

---

## 🚀 Key Design Principles

✔ Stateless services  
✔ Use caching  
✔ Use connection pooling  
✔ Monitor performance  
✔ Handle failures gracefully  
✔ Use logging & observability  

---

## 🎯 Interview Questions

**Q: What is system design?**

Designing scalable and reliable backend architecture.

---

**Q: Horizontal vs Vertical scaling?**

Vertical → Increase machine power  
Horizontal → Add more machines  

---

**Q: What is CAP theorem?**

Trade-off between Consistency, Availability, and Partition tolerance.

---

**Q: What is a load balancer?**

Distributes traffic across servers.

---

**Q: What is a single point of failure?**

A component that can bring entire system down.

---

## ✅ Key Takeaway

Good system design ensures:

✔ Scalability  
✔ Reliability  
✔ Performance  
✔ Maintainability  

Backend engineers must think beyond just code —  
they must design systems that grow.

✨ End of Day 12