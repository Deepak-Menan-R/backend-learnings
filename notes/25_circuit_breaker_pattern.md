# Day 25 – Circuit Breaker Pattern

## ⚡ What is the Circuit Breaker Pattern?

The **Circuit Breaker Pattern** is a design pattern used in distributed systems to prevent repeated failures when a service is unavailable or failing.

It works similarly to an **electrical circuit breaker**.

If a service starts failing repeatedly, the circuit breaker **stops sending requests temporarily** to prevent system overload.

Goal:

- Prevent cascading failures
- Improve system stability
- Reduce unnecessary load
- Enable graceful recovery

---

## 🧠 Why Circuit Breakers are Needed

In microservices architecture, services often depend on other services.

Example:


Client → API Service → Payment Service → Database


If **Payment Service fails**, the API service may continue sending requests.

Problems:

❌ Increased latency  
❌ Resource exhaustion  
❌ System-wide failure  

Circuit breakers prevent this scenario.

---

## 🔁 Circuit Breaker States

A circuit breaker typically has **three states**.

### 1️⃣ Closed State

Normal operation.

Requests flow normally to the service.


Client → Service → Response


Failures are monitored.

---

### 2️⃣ Open State

Triggered when failure threshold is exceeded.

All requests are immediately rejected.


Client → Circuit Breaker → Request Rejected


No requests reach the failing service.

This protects the system.

---

### 3️⃣ Half-Open State

After a cooldown period, the circuit breaker allows **limited test requests**.

If successful:

✔ Circuit closes again.

If failures continue:

❌ Circuit returns to open state.

---

## 📊 Circuit Breaker State Flow


Closed → Open → Half-Open → Closed


Example flow:


Closed → Many failures → Open
Open → Wait timeout → Half-Open
Half-Open → Success → Closed
Half-Open → Failure → Open


---

## 📦 Example Scenario

API calling a payment service.

Without circuit breaker:


API → Payment Service (fails repeatedly)


System continues retrying.

With circuit breaker:


API → Circuit Breaker → Payment Service


If failures exceed threshold:


API → Circuit Breaker → Request Blocked


---

## ⚙ Example Failure Threshold

Example configuration:

- Failure threshold: 5 failures
- Timeout: 30 seconds
- Retry attempts: 1

Meaning:

If 5 consecutive failures occur, the circuit opens for 30 seconds.

---

## 🧩 Fallback Mechanism

Circuit breakers often use **fallback responses**.

Example:

If payment service fails:


Return: "Payment service temporarily unavailable"


Or:


Use cached data


Fallback improves user experience.

---

## 🚀 Benefits of Circuit Breakers

✔ Prevent cascading failures  
✔ Improve system resilience  
✔ Reduce latency during failures  
✔ Protect backend services  
✔ Enable graceful degradation  

---

## 🛠 Real-World Circuit Breaker Tools

Common libraries implementing this pattern:

- Netflix Hystrix
- Resilience4j
- Envoy Proxy
- Istio Service Mesh

---

## ⚠ Common Mistakes

❌ No fallback strategy  
❌ Incorrect failure thresholds  
❌ No monitoring of circuit state  
❌ Too aggressive timeouts  

Proper configuration is important.

---

## 🎯 Interview Questions

**Q: What is the circuit breaker pattern?**

A pattern used to stop requests to a failing service to prevent system overload.

---

**Q: What are the three states of a circuit breaker?**

Closed, Open, and Half-Open.

---

**Q: Why use circuit breakers in microservices?**

To prevent cascading failures between dependent services.

---

**Q: What is a fallback in circuit breaker pattern?**

A backup response when a service is unavailable.

---

## ✅ Key Takeaway

Circuit breakers improve **system resilience** by preventing repeated failures from cascading through distributed systems.

They are essential for building **fault-tolerant microservices architectures**.

✨ End of Day 25