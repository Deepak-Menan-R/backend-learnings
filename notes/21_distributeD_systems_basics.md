# Day 21 – Distributed Systems Basics

## 🌐 What is a Distributed System?

A **distributed system** is a system where multiple independent computers (nodes) work together and appear to users as a single system.

Instead of running everything on one machine, the workload is distributed across multiple machines.

Goal:

- Improve scalability
- Increase reliability
- Handle large workloads
- Enable fault tolerance

---

## 🧠 Why Distributed Systems are Used

Modern applications must handle:

- Millions of users
- Massive data volumes
- High availability requirements

A single machine cannot handle these efficiently.

Distributed systems provide:

✔ Horizontal scalability  
✔ Fault tolerance  
✔ High availability  
✔ Better performance  

---

## 📦 Example Distributed System

Example architecture:


Client → Load Balancer → Multiple Application Servers → Distributed Database


Example:

       Client
         |
   Load Balancer
    /     |     \

Server1 Server2 Server3
|
Distributed DB


Each component works together as one system.

---

## ⚙ Key Characteristics of Distributed Systems

### 1️⃣ Scalability

Ability to handle increasing workloads by adding more machines.

Example:


Add more servers to handle more users


---

### 2️⃣ Fault Tolerance

System continues to work even if some components fail.

Example:


If Server2 fails → traffic routed to Server1 and Server3


---

### 3️⃣ High Availability

System remains operational most of the time.

Example:


99.99% uptime


Achieved using:

- Replication
- Load balancing
- Redundant systems

---

### 4️⃣ Transparency

Users interact with the system as if it were a single machine.

They do not see the distributed complexity.

---

## 🔄 Types of Distributed Architectures

### Client–Server Architecture

Traditional model.


Client → Server


---

### Microservices Architecture

Application divided into small independent services.

Example:


User Service
Order Service
Payment Service
Notification Service


Each service runs independently.

---

### Peer-to-Peer Architecture

All nodes act as both client and server.

Example:

- BitTorrent
- Blockchain networks

---

## 📊 Challenges in Distributed Systems

Building distributed systems introduces challenges:

❌ Network latency  
❌ Data consistency issues  
❌ Partial system failures  
❌ Complex debugging  
❌ Synchronization problems  

These problems make distributed systems harder to design.

---

## 🔁 Consistency Models

Distributed systems must decide how consistent data should be.

Two common models:

### Strong Consistency

All users see the same data immediately.

Example:


Bank account balance updates instantly everywhere


---

### Eventual Consistency

Data will become consistent after some time.

Example:


Social media likes count updating after a delay


---

## ⚠ Network Partition

A **network partition** occurs when nodes cannot communicate due to network failures.

Example:


Server1 cannot communicate with Server2


System must decide whether to prioritize:

- Consistency
- Availability

This relates to **CAP Theorem**.

---

## 🚀 Real-World Distributed Systems

Examples of distributed systems:

- Google Search
- Amazon Web Services
- Netflix
- Facebook
- Kubernetes clusters

These systems run across thousands of machines.

---

## ⚠ Common Mistakes

❌ Ignoring network failures  
❌ Assuming communication is reliable  
❌ Poor monitoring and observability  
❌ Tight coupling between services  

---

## 🎯 Interview Questions

**Q: What is a distributed system?**

A system where multiple machines work together to function as one system.

---

**Q: Why use distributed systems?**

To improve scalability, availability, and fault tolerance.

---

**Q: What are common challenges in distributed systems?**

Network latency, partial failures, and consistency issues.

---

**Q: What is eventual consistency?**

Data becomes consistent across nodes after some time.

---

## ✅ Key Takeaway

Distributed systems enable modern large-scale applications by providing:

✔ Scalability  
✔ Reliability  
✔ High availability  
✔ Fault tolerance  

However, they introduce complexity that must be carefully managed.

✨ End of Day 21