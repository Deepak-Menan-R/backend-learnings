Here's a **Day 43 – Polling** note in the same format as your WebSockets notes:

# Day 43 – Polling

## 📜 What is Polling?

**Polling** is a technique where the client repeatedly sends requests to the server at fixed intervals to check for new data.

👉 Client asks the server repeatedly
👉 Server responds with the latest available data
👉 Connection closes after every request-response cycle

---

## 🧠 Why Polling?

In traditional HTTP:

Client → Request
Server → Response

Since the server cannot send updates on its own, the client must keep checking for changes.

Polling helps applications receive updated information periodically.

---

## 🔁 How Polling Works

1️⃣ Client sends a request to the server

2️⃣ Server returns the current data

3️⃣ Client waits for a fixed interval

4️⃣ Client sends another request

5️⃣ Process repeats continuously

---

## 📦 Example – Chat Application

### With Polling

Client requests new messages every 2 seconds.

Flow:

Client → Server → Messages
(wait 2 sec)
Client → Server → Messages

Problems:

❌ Messages may be delayed until the next poll
❌ Many unnecessary requests when no new data exists

---

## ⚙ Polling Connection Flow

Client Request

GET /messages

Server Response

200 OK

Latest Messages

Connection Closed

Client waits and sends another request later.

---

## 🔄 Communication Flow

Client → Server

(wait interval)

Client → Server

(wait interval)

Client → Server

The server only responds when asked.

---

## 🧩 Polling vs WebSockets

| Feature           | Polling           | WebSockets    |
| ----------------- | ----------------- | ------------- |
| Connection        | Repeated Requests | Persistent    |
| Communication     | Client Initiated  | Bidirectional |
| Latency           | Higher            | Low           |
| Network Usage     | Higher            | Efficient     |
| Real-time Support | Moderate          | Excellent     |

---

## 📊 Benefits of Polling

✔ Easy to implement

✔ Works with standard HTTP

✔ No special protocol required

✔ Compatible with most infrastructures

✔ Useful for infrequent updates

---

## ⚠ Challenges of Polling

❌ Increased network traffic

❌ Higher latency

❌ Many unnecessary requests

❌ Wastes server resources

❌ Poor scalability at high frequency

---

## 🚀 Polling Lifecycle

### Request Cycle

1️⃣ Send Request

2️⃣ Receive Response

3️⃣ Wait Interval

4️⃣ Send Next Request

5️⃣ Repeat

---

## 🧠 Polling Strategy

Common polling intervals:

* 1 second → Near real-time updates
* 5 seconds → Moderate updates
* 30 seconds → Low-frequency updates

Choosing the right interval balances responsiveness and resource usage.

---

## ⚙ Scaling Polling

For large systems:

✔ Caching

✔ Rate limiting

✔ Efficient APIs

✔ Load balancing

✔ Optimized polling intervals

---

## 📦 Popular Use Cases

✔ Email refresh

✔ Weather updates

✔ News feeds

✔ System monitoring

✔ Status tracking

✔ Background synchronization

---

## ⚠ Common Mistakes

❌ Polling too frequently

❌ Ignoring server load

❌ Requesting large payloads repeatedly

❌ Using polling for highly real-time applications

❌ Not implementing request throttling

---

## 🛠 Example Flow – Order Tracking

User checks order status
↓
Client sends request
↓
Server returns latest status
↓
Client waits 10 seconds
↓
Client requests again

---

## 🎯 Interview Questions

**Q: What is polling?**

A technique where a client repeatedly sends requests to the server at regular intervals to check for updates.

---

**Q: How does polling work?**

The client periodically sends HTTP requests, and the server responds with the latest available data.

---

**Q: What are the drawbacks of polling?**

Higher latency, unnecessary requests, increased network usage, and poor scalability for real-time systems.

---

**Q: When should polling be used?**

When updates are infrequent and implementing real-time communication is unnecessary.

---

**Q: How is polling different from WebSockets?**

Polling requires repeated client requests, while WebSockets maintain a persistent connection allowing instant bidirectional communication.

---

## ✅ Key Takeaway

Polling enables:

✔ Periodic data updates

✔ Simple implementation using HTTP

✔ Compatibility with existing systems

However, it introduces:

❌ Higher latency

❌ Extra network overhead

❌ Unnecessary requests

Polling is best suited for applications where updates are **occasional rather than truly real-time**.

✨ End of Day 43
