# Day 15 – API Documentation

## 📘 What is API Documentation?

**API Documentation** is a structured explanation of how an API works and how developers can use it.

It describes:

- Available endpoints
- Request formats
- Response formats
- Authentication requirements
- Error responses

Good API documentation helps developers **integrate quickly and correctly**.

---

## 🧠 Why API Documentation is Important

Without documentation:

❌ Developers struggle to understand APIs  
❌ Integration takes longer  
❌ Increased support requests  
❌ Misuse of endpoints  

With proper documentation:

✔ Faster onboarding  
✔ Better developer experience  
✔ Easier maintenance  
✔ Clear communication between teams  

---

## 📦 What Should API Documentation Include?

A good API documentation should contain:

- Base URL
- Authentication method
- Available endpoints
- Request parameters
- Request body structure
- Response format
- Error responses
- Rate limits
- Example requests & responses

---

## 🌐 Base URL

The **Base URL** is the root endpoint for all API calls.

Example:

https://api.example.com/v1


All API requests start with this base.

Example endpoint:

GET https://api.example.com/v1/users


---

## 🔐 Authentication Information

Documentation must explain **how to authenticate requests**.

Example:

Authorization: Bearer <token>

Example request:

GET /users
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...


---

## 📡 Endpoint Documentation Example

### Get All Users

**Endpoint**

GET /users


**Description**

Returns a list of all users.

**Request Example**

GET /users
Authorization: Bearer TOKEN


**Response Example**

```json
[
  {
    "id": 1,
    "name": "Deepak",
    "email": "deepak@email.com"
  }
]

📦 Request Body Example

For creating resources.

Example:

POST /users

Request body:

{
  "name": "Deepak",
  "email": "deepak@email.com"
}

📬 Response Structure

A typical API response contains:

Data

Status

Optional message

Example:

{
  "status": "success",
  "data": {
    "id": 1,
    "name": "Deepak"
  }
}

⚠ Error Response Documentation

Errors should be clearly documented.

Example:

{
  "error": "Validation Error",
  "message": "Email field is required"
}

| Code | Meaning               |
| ---- | --------------------- |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |

📊 Documenting Query Parameters

Example endpoint:

GET /products?category=electronics&page=2

Parameters:

| Parameter | Type    | Description                 |
| --------- | ------- | --------------------------- |
| category  | string  | Filter products by category |
| page      | integer | Page number                 |

🧰 Popular API Documentation Tools

Common tools used in backend development:

Swagger / OpenAPI

Postman Documentation

Redoc

Stoplight

These tools generate interactive API documentation.

🚀 Swagger / OpenAPI (Industry Standard)

Swagger allows developers to:

✔ Define APIs using OpenAPI specification
✔ Generate interactive documentation
✔ Test endpoints directly

Example Swagger UI features:

Try API requests

View request schemas

View response schemas

⚠ Common Documentation Mistakes

❌ Missing examples
❌ Outdated documentation
❌ Inconsistent formats
❌ Missing error descriptions
❌ No authentication explanation

✅ Key Takeaway

Good API documentation ensures:

✔ Clear communication
✔ Faster integration
✔ Better developer experience
✔ Easier maintenance

Well-documented APIs are easier to adopt and maintain.

✨ End of Day 15
