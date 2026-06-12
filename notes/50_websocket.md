# Day 50 – WebSockets

## 📜 What are WebSockets?

**WebSockets** provide a **persistent, full-duplex communication channel** between client and server over a single TCP connection.

👉 Unlike HTTP, the connection stays open
👉 Both client and server can send data anytime

---

## 🧠 Why WebSockets?

Traditional HTTP:

Client → Request
Server → Response

Problem:

❌ Repeated polling
❌ High latency
❌ Inefficient for real-time apps

With WebSockets:

Client ⇄ Server (continuous connection)

✔ Real-time communication
✔ Low latency
✔ Efficient bidirectional messaging

---

## 🔁 How WebSockets Work

1️⃣ Client sends WebSocket handshake request
2️⃣ Server upgrades HTTP connection
3️⃣ Persistent connection established
4️⃣ Data flows both ways in real time

---

## 📦 Example – Chat Application

### Without WebSockets

Client polls server every 2 sec

Problems:

❌ Delayed messages
❌ Too many requests

---

### With WebSockets

Client ⇄ Server

Messages appear instantly.

---

## ⚙ WebSocket Connection Flow

HTTP Request
Upgrade: websocket

Server response:

101 Switching Protocols

Connection upgraded successfully.

---

## 🔄 Communication Flow

Client ⇄ WebSocket Server ⇄ Other Clients

Steps:

1️⃣ Client connects
2️⃣ Server keeps connection open
3️⃣ Messages sent instantly
4️⃣ Server broadcasts updates

---

## 🧩 WebSockets vs HTTP

| Feature           | HTTP        | WebSockets |
| ----------------- | ----------- | ---------- |
| Connection        | Short-lived | Persistent |
| Communication     | One-way     | Two-way    |
| Latency           | Higher      | Low        |
| Real-time support | Poor        | Excellent  |

---

## 📊 Benefits of WebSockets

✔ Real-time communication
✔ Low network overhead
✔ Faster updates
✔ Efficient for live applications
✔ Reduces unnecessary polling

---

## ⚠ Challenges of WebSockets

❌ Connection management complexity
❌ Scaling persistent connections
❌ Harder load balancing
❌ Requires reconnect handling

---

## 🚀 WebSocket Lifecycle

### Connection States

1️⃣ Connecting
2️⃣ Open
3️⃣ Closing
4️⃣ Closed

---

## 🧠 Reconnection Strategy

If connection drops:

✔ Retry connection
✔ Exponential backoff
✔ Heartbeats/ping-pong checks

Example:

Retry after:
1s → 2s → 4s → 8s

---

## ⚙ Scaling WebSockets

For large systems:

✔ Load balancers
✔ Sticky sessions
✔ Distributed message brokers (Kafka/Redis PubSub)

---

## 📦 Popular Use Cases

✔ Chat applications
✔ Live notifications
✔ Multiplayer games
✔ Stock market apps
✔ Collaborative editing
✔ Real-time dashboards

---

## ⚠ Common Mistakes

❌ Opening too many connections
❌ No reconnect strategy
❌ Ignoring heartbeat mechanism
❌ Sending huge messages frequently
❌ Using WebSockets when polling is enough

---

## 🛠 Example Flow – Live Chat

User A sends message
↓
Server receives message
↓
Server pushes message to User B instantly

---

## 🎯 Interview Questions

**Q: What are WebSockets?**

A persistent bidirectional communication protocol for real-time applications.

---

**Q: How are WebSockets different from HTTP?**

HTTP is request-response based, while WebSockets allow continuous two-way communication.

---

**Q: What is the WebSocket handshake?**

An HTTP upgrade request that converts HTTP into a WebSocket connection.

---

**Q: Why are WebSockets useful?**

They provide low-latency real-time communication.

---

**Q: What are common WebSocket use cases?**

Chats, gaming, notifications, dashboards, and collaborative apps.

---

## ✅ Key Takeaway

WebSockets enable:

✔ Persistent connections
✔ Real-time bidirectional communication
✔ Low-latency data transfer

They are best suited for **interactive real-time systems**.

✨ End of Day 50
