# Day 42 – Saga Pattern (Distributed Transactions)

## 🔄 What is the Saga Pattern?

The **Saga Pattern** is a design pattern used to manage **distributed transactions** across multiple services.

Instead of using a single ACID transaction, a saga breaks a transaction into **a sequence of smaller local transactions**.

Each step:

✔ Executes independently  
✔ Has a **compensating action** in case of failure  

---

## 🧠 Why Saga Pattern is Needed

In microservices:

- Each service has its own database  
- Distributed transactions are difficult  

Traditional approach (2PC):

❌ Slow  
❌ Blocking  
❌ Not scalable  

Saga solves this by:

✔ Avoiding global locks  
✔ Using eventual consistency  
✔ Handling failures gracefully  

---

## 📦 Example Problem

E-commerce order flow:

Create Order
Deduct Inventory
Process Payment

If payment fails:

❌ Order created but not paid  
❌ Inventory already deducted  

System becomes inconsistent.

---

## 🚀 Solution with Saga

Each step has a **compensation step**.

Example:

Create Order → Compensate: Cancel Order
Deduct Inventory → Compensate: Restore Inventory
Process Payment → Compensate: Refund Payment

---

## 🔁 Saga Execution Flow


Step1 → Step2 → Step3
| | |
Comp1 Comp2 Comp3


If any step fails:

👉 Execute compensating actions in reverse order.

---

## 🧩 Types of Saga Pattern

---

## 1️⃣ Choreography-Based Saga

### 📌 Concept

Services communicate via **events**.

No central controller.

Example flow:


Order Service → Event → Inventory Service → Event → Payment Service


### ✅ Advantages

✔ Decoupled  
✔ Easy to scale  

### ❌ Disadvantages

❌ Hard to track flow  
❌ Complex debugging  

---

## 2️⃣ Orchestration-Based Saga

### 📌 Concept

A central **orchestrator** controls the flow.

Example:


Orchestrator → Order → Inventory → Payment


### ✅ Advantages

✔ Clear flow control  
✔ Easier debugging  

### ❌ Disadvantages

❌ Central dependency  
❌ Slightly less flexible  

---

## 🔄 Failure Handling

If step fails:

Example:


Step1 ✔
Step2 ✔
Step3 ❌


Compensation:


Undo Step2
Undo Step1


---

## ⚠ Eventual Consistency

Saga does NOT guarantee immediate consistency.

✔ Data becomes consistent eventually  

---

## 🚀 Benefits of Saga Pattern

✔ Scalable distributed transactions  
✔ No global locks  
✔ Fault-tolerant  
✔ Works well with microservices  

---

## ⚠ Challenges

❌ Complex implementation  
❌ Managing compensations  
❌ Debugging distributed flows  
❌ Handling partial failures  

---

## 🛠 Real-World Use Cases

✔ E-commerce systems  
✔ Payment processing  
✔ Booking systems (flights, hotels)  
✔ Order management systems  

---

## ⚠ Common Mistakes

❌ Not designing proper compensating actions  
❌ Ignoring failure scenarios  
❌ Overcomplicating simple workflows  

---

## 🎯 Interview Questions

**Q: What is Saga pattern?**

A pattern to manage distributed transactions using a sequence of local transactions.

---

**Q: Choreography vs Orchestration?**

Choreography → Event-based, no central control  
Orchestration → Central controller manages flow  

---

**Q: What is a compensating transaction?**

An action that undoes a previous step.

---

**Q: Does Saga guarantee strong consistency?**

❌ No → It provides eventual consistency  

---

## ✅ Key Takeaway

Saga Pattern enables **reliable distributed transactions** in microservices by:

✔ Breaking operations into steps  
✔ Handling failures with compensation  
✔ Ensuring eventual consistency  

✨ End of Day 42