# Day 41 – Event Sourcing

## 📜 What is Event Sourcing?

**Event Sourcing** is an architectural pattern where the system stores **all changes as a sequence of events**, instead of just storing the current state.

👉 Instead of storing "what the data is",  
👉 We store "what happened to the data".

---

## 🧠 Why Event Sourcing?

Traditional approach:


Update balance → Store new balance = 900


Problem:

❌ No history  
❌ Hard to debug  
❌ Cannot reconstruct past state  

With Event Sourcing:


BalanceCreated(1000)
BalanceDebited(100)


✔ Full history available  
✔ Easy debugging  
✔ Time travel possible  

---

## 🔁 How Event Sourcing Works

1️⃣ Every change is stored as an **event**  
2️⃣ Events are appended (never deleted)  
3️⃣ Current state is derived by replaying events  

---

## 📦 Example – Bank Account

### Events Stored


AccountCreated(1000)
MoneyWithdrawn(200)
MoneyDeposited(500)


---

### Reconstruct State


1000 - 200 + 500 = 1300


Current balance = **1300**

---

## ⚙ Event Store

Events are stored in an **append-only log**.

Characteristics:

✔ Immutable  
✔ Ordered  
✔ Durable  

Example storage:


Event1 → Event2 → Event3 → Event4


---

## 🔄 Event Flow


Command → Event → Event Store → Read Model


Steps:

1️⃣ Command received  
2️⃣ Event generated  
3️⃣ Event stored  
4️⃣ Read model updated  

---

## 🧩 Event Sourcing + CQRS

Often used together:

- **CQRS** → Separate read/write  
- **Event Sourcing** → Store events instead of state  

---

## 📊 Benefits of Event Sourcing

✔ Complete audit log  
✔ Debugging & traceability  
✔ Replay system state  
✔ Supports temporal queries  
✔ Easy integration with event-driven systems  

---

## ⚠ Challenges of Event Sourcing

❌ Complex implementation  
❌ Event schema evolution  
❌ Storage growth  
❌ Rebuilding state can be slow  

---

## 🚀 Snapshotting (Optimization)

To avoid replaying all events:

✔ Store periodic snapshots  

Example:


Snapshot: balance = 1000
Events after snapshot:
+200, -50


Final state:


1000 + 200 - 50 = 1150


---

## 🧠 Real-World Use Cases

✔ Banking systems  
✔ Financial transactions  
✔ Audit systems  
✔ Order tracking systems  

---

## ⚠ Common Mistakes

❌ Using event sourcing for simple systems  
❌ Not handling event versioning  
❌ Ignoring storage growth  
❌ No snapshot strategy  

---

## 🎯 Interview Questions

**Q: What is event sourcing?**

Storing state changes as events instead of current state.

---

**Q: Why use event sourcing?**

To maintain history and enable system replay.

---

**Q: What is an event store?**

A database storing all events in order.

---

**Q: What is snapshotting?**

Saving current state to avoid replaying all events.

---

## ✅ Key Takeaway

Event Sourcing provides:

✔ Full system history  
✔ Better traceability  
✔ Powerful debugging capabilities  

It is best suited for **complex, audit-heavy systems**.

✨ End of Day 41