# Day 06 – Error Handling in Backend Systems

## ⚠️ What is Error Handling?

**Error handling** is the process of detecting, managing, and responding to runtime issues  
that occur during request processing.

Goal:

👉 Prevent application crashes  
👉 Return meaningful responses  
👉 Improve reliability & debugging  

---

## 🧠 Why Error Handling Matters

Without proper handling:

❌ Server crashes  
❌ Poor user experience  
❌ Debugging nightmare  

With proper handling:

✔ Graceful failures  
✔ Clear error messages  
✔ Stable systems  

---

## 🔁 Where Errors Can Occur

Errors may happen in:

- Input validation
- Database queries
- External API calls
- Authentication
- Business logic
- Network issues

---

## 📦 Types of Errors

### ✅ Client Errors (4xx)

Problem caused by client request.

Examples:

- Invalid input
- Unauthorized access
- Resource not found

---

### ✅ Server Errors (5xx)

Problem caused by backend/system.

Examples:

- Database failure
- Unhandled exception
- Timeout

---

## 🎯 Common HTTP Error Codes

| Code | Meaning |
|------|----------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Unprocessable Entity |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

---

## 🧠 Good Error Response Structure

A well-designed API returns structured errors.

Example:

```json
{
  "error": "Invalid input",
  "message": "Email field is required",
  "status": 400
}

🛠 Basic Error Handling Logic

TRY
    Execute operation

IF error occurs
    Catch exception
    Return proper error response

🧩 Validation Error Example

Scenario:

Client sends incomplete request.

Request

POST /users
Body:
{
  "name": "Deepak"
}

Response

400 Bad Request
{
  "error": "Validation Error",
  "message": "Email is required"
}

🧩 Not Found Example

Request

GET /users/999

Response

404 Not Found
{
  "error": "Resource Not Found",
  "message": "User does not exist"
}

🛡 Try–Catch / Exception Handling

Used to prevent crashes.

Concept:

✔ Catch unexpected failures
✔ Log errors
✔ Return safe responses

🧾 Logging Errors (CRITICAL)

Always log errors internally.

Log:

Error message

Stack trace

Endpoint

Timestamp

Avoid exposing:

❌ Internal stack traces to clients

⚠️ Bad Practice Example

❌ Returning raw exception:

500 Internal Server Error
NullPointerException at line 42

✅ Good Practice Example

✔ Generic client response:

{
  "error": "Internal Server Error",
  "message": "Something went wrong"
}

🔄 Global Error Handling

Centralized error management.

Benefits:

✔ Cleaner routes
✔ Consistent responses
✔ Easier maintenance

⚠️ Common Error Handling Mistakes

❌ Ignoring exceptions
❌ Wrong status codes
❌ Exposing sensitive info
❌ Inconsistent error format
❌ No logging

🚀 Best Practices

✔ Use correct HTTP status codes
✔ Return structured error responses
✔ Log errors properly
✔ Use global handlers
✔ Fail gracefully