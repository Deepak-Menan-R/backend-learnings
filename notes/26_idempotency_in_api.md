# Day 26 – Idempotency in APIs

## 🔁 What is Idempotency?

**Idempotency** means that performing the same operation multiple times produces the **same result as performing it once**.

In APIs, an operation is idempotent if repeating the same request does **not change the result beyond the initial execution**.

Goal:

- Prevent duplicate operations
- Handle retries safely
- Ensure system consistency

---

## 🧠 Why Idempotency is Important

In real systems, requests may be retried due to:

- Network failures
- Client retries
- Timeouts
- Load balancer retries

Without idempotency:

❌ Duplicate transactions  
❌ Multiple payments  
❌ Data inconsistency  

With idempotency:

✔ Safe retries  
✔ Consistent system behavior  
✔ Reliable APIs  

---

## 📦 Example Problem

A user makes a payment request:


POST /payments


Network fails before response arrives.

Client retries request.

Without idempotency:


Payment processed twice ❌


User charged twice.

With idempotency:


Payment processed once ✔


---

## ⚙ Idempotent HTTP Methods

Some HTTP methods are **naturally idempotent**.

| Method | Idempotent | Explanation |
|------|------------|-------------|
| GET | Yes | Fetching data does not change state |
| PUT | Yes | Replacing resource results in same state |
| DELETE | Yes | Deleting again has no effect |
| POST | No | Usually creates new resource |

---

## 🧩 Example of Idempotent Request

### PUT Example


PUT /users/10


Body:

```json
{
  "name": "Deepak"
}

Sending this request multiple times results in:

User name = Deepak

No additional changes.

❌ Example of Non-Idempotent Request
POST Example
POST /orders

Body:

{
  "product": "Laptop"
}

Sending request twice:

Order #101 created
Order #102 created

Duplicate orders occur.

🔑 Idempotency Keys

To make non-idempotent operations safe, APIs use idempotency keys.

An idempotency key is a unique identifier sent with a request.

Example header:

Idempotency-Key: abc123xyz
🔄 Idempotency Flow

1️⃣ Client sends request with idempotency key

POST /payments
Idempotency-Key: abc123

2️⃣ Server checks if key exists

If new → process request

If duplicate → return previous result

📊 Example Idempotent Payment Flow

First request:

POST /payments
Idempotency-Key: payment123

Server processes payment.

Second identical request:

POST /payments
Idempotency-Key: payment123

Server returns stored result instead of processing again.

🚀 Benefits of Idempotency

✔ Prevent duplicate operations
✔ Safe retries
✔ Reliable distributed systems
✔ Better fault tolerance

⚠ Common Mistakes

❌ Ignoring duplicate requests
❌ No idempotency keys for payments
❌ Not storing request results
❌ Poor retry handling

🛠 Real-World Use Cases

Idempotency is critical for:

Payment processing

Order creation

Financial transactions

Distributed message processing

Example systems:

Stripe API

PayPal APIs

🎯 Interview Questions

Q: What is idempotency?

An operation that produces the same result even if executed multiple times.

Q: Which HTTP methods are idempotent?

GET, PUT, DELETE.

Q: Why is idempotency important in payments?

To prevent duplicate transactions.

Q: What is an idempotency key?

A unique key used to detect duplicate requests.

✅ Key Takeaway

Idempotency ensures APIs behave safely under retries and failures.

It is essential for building reliable and fault-tolerant backend systems.

✨ End of Day 26