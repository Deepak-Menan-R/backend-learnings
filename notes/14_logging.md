# Day 14 – Logging & Observability

## 📜 What is Logging?

**Logging** is the process of recording important events, errors, and system activities  
during application execution.

Logs help developers:

👉 Debug issues  
👉 Monitor behavior  
👉 Trace failures  
👉 Understand production problems  

---

## 🧠 Why Logging is Important

Without logging:

❌ Hard to debug production issues  
❌ No visibility into failures  
❌ Poor monitoring  

With proper logging:

✔ Easier debugging  
✔ Faster issue resolution  
✔ Better system understanding  

---

## 📦 What Should Be Logged?

Common things to log:

- Incoming requests
- Response status
- Errors & exceptions
- Authentication failures
- Database errors
- External API calls
- Important business events

---

## 🔢 Log Levels (VERY IMPORTANT)

| Level   | Purpose |
|----------|----------|
| DEBUG   | Detailed internal info |
| INFO    | General operational messages |
| WARNING | Something unexpected but not fatal |
| ERROR   | Failed operation |
| CRITICAL| Severe system failure |

---

## 🛠 Example Logs

### INFO Log

[INFO] User login successful | user_id=101

### ERROR Log

[ERROR] Database connection failed


---

## ⚠ Logging Best Practices

✔ Use appropriate log levels  
✔ Avoid logging sensitive data  
✔ Include timestamps  
✔ Log structured data  
✔ Keep logs readable  
✔ Centralize logs  

---

## 🚫 Never Log Sensitive Data

❌ Passwords  
❌ JWT tokens  
❌ Credit card numbers  
❌ Personal data  

Security risk 🚨

---

## 📊 Structured Logging

Instead of plain text:

Bad:

User failed login


Good:
```json
{
  "level": "ERROR",
  "message": "Login failed",
  "user_id": 101,
  "timestamp": "2026-03-03T10:00:00Z"
}

Benefits:

✔ Machine readable
✔ Searchable
✔ Filterable

🔍 What is Observability?

Observability is the ability to understand the internal state
of a system using external outputs.

It consists of:

1️⃣ Logs
2️⃣ Metrics
3️⃣ Traces

📈 Metrics

Metrics are numerical measurements.

Examples:

CPU usage

Memory usage

Request latency

Error rate

Requests per second (RPS)

🔗 Tracing

Tracing tracks a request across services.

Example:

User → API → Auth Service → DB → Payment Service

Helps identify:

✔ Bottlenecks
✔ Slow components
✔ Failure points

🚀 Logging in Scalable Systems

In production systems:

✔ Logs stored centrally
✔ Use log aggregation tools
✔ Use monitoring dashboards
✔ Set alerts for errors

⚠ Common Logging Mistakes

❌ Logging everything (noise)
❌ Logging nothing
❌ Logging sensitive data
❌ Not rotating logs
❌ No monitoring

✅ Key Takeaway

Logging & observability ensure:

✔ System visibility
✔ Faster debugging
✔ Better reliability
✔ Production readiness

Backend systems without logging are blind.

✨ End of Day 14