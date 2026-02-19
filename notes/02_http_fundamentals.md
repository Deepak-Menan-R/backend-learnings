# Day 02 – HTTP Fundamentals

## 🌐 What is HTTP?

**HTTP (HyperText Transfer Protocol)** is the foundation of communication on the web.  
It defines how clients and servers exchange data.

HTTP is:

- Stateless
- Request–Response based
- Application layer protocol
- Human-readable (text-based)

---

## 🔁 HTTP Communication Model

HTTP follows a **client → server → response** model.

1️⃣ Client sends a request  
2️⃣ Server processes it  
3️⃣ Server sends a response  

Example:

Client → `GET /users`  
Server → `200 OK + Data`

---

## 📦 Structure of an HTTP Request

An HTTP request contains:

- Method
- URL (Endpoint)
- Headers
- Optional Body

---

### ✅ Example Request

POST /users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer token123

{
"name": "Deepak"
}

---

## 📬 Components Explained

### 1️⃣ Method
Defines the action.

Examples:

- GET → Retrieve
- POST → Create
- PUT → Replace
- DELETE → Remove

---

### 2️⃣ URL / Endpoint
Specifies the resource.

/users
/products/10
/orders/123

---

### 3️⃣ Headers
Metadata about the request.

Common headers:

- Content-Type
- Authorization
- Accept
- User-Agent

Example:

Content-Type: application/json
Authorization: Bearer token

---

### 4️⃣ Body (Optional)
Contains payload data (POST / PUT / PATCH).

Usually JSON:

```json
{
  "name": "Deepak"
}

## 📦 Structure of an HTTP Response

An HTTP response contains:

- Status line  
- Headers  
- Optional Body  

**Example Response**

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 45


**Response Body**
```json
{
  "id": 1,
  "name": "Deepak"
}


📊 HTTP Status Line

Format: HTTP-Version Status-Code Reason

Example:

HTTP/1.1 200 OK

📦 Status Code Categories

| Range | Meaning       |
| ----- | ------------- |
| 1xx   | Informational |
| 2xx   | Success       |
| 3xx   | Redirection   |
| 4xx   | Client Error  |
| 5xx   | Server Error  |

✅ Common Status Codes

| Code | Meaning      |
| ---- | ------------ |
| 200  | OK           |
| 201  | Created      |
| 204  | No Content   |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |
| 500  | Server Error |

🔁 Statelessness (Important Concept)

HTTP is stateless:

Server does not remember previous requests

Each request is independent

State handled via:

Tokens

Cookies

Sessions (app-level)


🍪 Cookies vs Tokens
Cookies

Stored in browser

Sent automatically

Tokens

Stored client-side

Sent via headers

Example: Authorization: Bearer JWT_TOKEN

