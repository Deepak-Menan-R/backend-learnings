# REST API in Web Development

## Table of Contents

* [Introduction](#introduction)
* [What is REST API](#what-is-rest-api)
* [Why REST APIs are Needed](#why-rest-apis-are-needed)
* [How REST APIs Work](#how-rest-apis-work)
* [Client-Server Architecture](#client-server-architecture)
* [REST Principles](#rest-principles)
* [HTTP Methods in REST](#http-methods-in-rest)
* [REST API Request Structure](#rest-api-request-structure)
* [REST API Response Structure](#rest-api-response-structure)
* [HTTP Status Codes in REST APIs](#http-status-codes-in-rest-apis)
* [Headers in REST APIs](#headers-in-rest-apis)
* [Authentication in REST APIs](#authentication-in-rest-apis)
* [CRUD Operations in REST APIs](#crud-operations-in-rest-apis)
* [JSON in REST APIs](#json-in-rest-apis)
* [API Versioning](#api-versioning)
* [Pagination](#pagination)
* [Filtering and Sorting](#filtering-and-sorting)
* [Error Handling](#error-handling)
* [Rate Limiting](#rate-limiting)
* [Caching in REST APIs](#caching-in-rest-apis)
* [REST API Best Practices](#rest-api-best-practices)
* [REST API Limitations](#rest-api-limitations)
* [REST vs SOAP](#rest-vs-soap)
* [REST vs GraphQL](#rest-vs-graphql)
* [REST API in Node.js](#rest-api-in-nodejs)
* [Real-World Example](#real-world-example)
* [Interview Questions](#interview-questions)
* [Key Takeaway](#key-takeaway)

---

# Introduction

REST APIs are the backbone of modern web applications.

Every time you:

* Login to an app
* Fetch user data
* Submit forms
* Load products
* Use mobile applications

REST APIs help clients communicate with servers.

REST APIs are widely used in:

* Web applications
* Mobile apps
* Cloud services
* Microservices
* Third-party integrations

---

# What is REST API

REST stands for:

```text
Representational State Transfer
```

A REST API is:

* An architectural style
* Based on HTTP protocol
* Stateless
* Client-server based
* Resource-oriented

REST APIs expose resources using URLs.

Example:

```text
/users
/products
/orders
```

---

# Why REST APIs are Needed

Modern applications need:

* Communication between frontend and backend
* Mobile app integration
* Scalable systems
* Standardized APIs
* Fast data exchange

Without APIs:

* Applications could not share data
* Frontend and backend could not communicate efficiently
* Third-party integrations would be difficult

REST became popular because it is simple and lightweight.

---

# How REST APIs Work

REST APIs follow:

```text
Client → Request → Server
Server → Response → Client
```

Example:

```text
Frontend sends API request
          ↓
Backend processes request
          ↓
Database operations occur
          ↓
Server sends JSON response
```

REST APIs commonly use:

```text
HTTP + JSON
```

---

# Client-Server Architecture

REST separates:

```text
Client ↔ Server
```

## Client

Responsible for:

* UI
* User interaction
* Sending requests

Examples:

* Browser
* Mobile app
* React frontend

---

## Server

Responsible for:

* Business logic
* Database operations
* Authentication
* Sending responses

Examples:

* Node.js
* Django
* Spring Boot

---

# REST Principles

REST APIs follow key principles.

---

## 1. Statelessness

Each request is independent.

Server does not store client state between requests.

---

## 2. Client-Server Separation

Frontend and backend are independent.

---

## 3. Resource-Based

Everything is treated as a resource.

Example:

```text
/users/1
/products/10
```

---

## 4. Uniform Interface

Standardized communication using HTTP methods.

---

## 5. Cacheable

Responses may be cached for better performance.

---

# HTTP Methods in REST

| Method | Purpose        |
| ------ | -------------- |
| GET    | Retrieve data  |
| POST   | Create data    |
| PUT    | Replace data   |
| PATCH  | Partial update |
| DELETE | Remove data    |

---

# GET Request Example

```http
GET /users HTTP/1.1
Host: api.example.com
```

Used for:

* Fetching users
* Reading resources
* Loading data

---

# POST Request Example

```http
POST /users HTTP/1.1
Content-Type: application/json

{
  "name": "Deepak",
  "email": "deepak@example.com"
}
```

Used for:

* Creating resources
* Form submissions
* Sending data

---

# PUT Request Example

```http
PUT /users/1 HTTP/1.1
Content-Type: application/json

{
  "name": "Updated Name"
}
```

Used for:

* Updating entire resource

---

# PATCH Request Example

```http
PATCH /users/1 HTTP/1.1
Content-Type: application/json

{
  "email": "new@example.com"
}
```

Used for:

* Partial updates

---

# DELETE Request Example

```http
DELETE /users/1 HTTP/1.1
```

Used for:

* Removing resources

---

# REST API Request Structure

A REST request contains:

```text
URL
Method
Headers
Body
```

Example:

```http
POST /api/users HTTP/1.1
Host: api.example.com
Authorization: Bearer token
Content-Type: application/json

{
  "name": "Deepak"
}
```

---

# REST API Response Structure

A response contains:

```text
Status Code
Headers
Response Body
```

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "success": true
}
```

---

# HTTP Status Codes in REST APIs

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 204  | No Content            |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 409  | Conflict              |
| 500  | Internal Server Error |

---

# Status Code Categories

| Range | Category      |
| ----- | ------------- |
| 1xx   | Informational |
| 2xx   | Success       |
| 3xx   | Redirection   |
| 4xx   | Client Errors |
| 5xx   | Server Errors |

---

# Headers in REST APIs

Headers provide metadata.

## Common Headers

| Header        | Purpose              |
| ------------- | -------------------- |
| Content-Type  | Data format          |
| Authorization | Authentication token |
| Accept        | Expected response    |
| Cache-Control | Caching rules        |
| User-Agent    | Client information   |

---

# JSON in REST APIs

REST APIs commonly use:

```text
JSON (JavaScript Object Notation)
```

Example:

```json
{
  "id": 1,
  "name": "Deepak",
  "email": "deepak@example.com"
}
```

Benefits:

* Lightweight
* Human-readable
* Easy parsing
* Language-independent

---

# CRUD Operations in REST APIs

| Operation | HTTP Method |
| --------- | ----------- |
| Create    | POST        |
| Read      | GET         |
| Update    | PUT/PATCH   |
| Delete    | DELETE      |

---

# Authentication in REST APIs

REST APIs support multiple authentication methods.

| Method       | Description          |
| ------------ | -------------------- |
| Basic Auth   | Username/password    |
| API Key      | Unique access key    |
| JWT          | Token-based auth     |
| OAuth        | Third-party login    |
| Session Auth | Cookie-based session |

---

# JWT Authentication Example

Client sends:

```http
Authorization: Bearer JWT_TOKEN
```

Server verifies token before processing request.

---

# API Versioning

Versioning helps maintain compatibility.

Example:

```text
/api/v1/users
/api/v2/users
```

Benefits:

* Backward compatibility
* Safer updates
* Easier maintenance

---

# Pagination

Pagination limits response size.

Example:

```http
GET /products?page=1&limit=10
```

Benefits:

* Faster APIs
* Reduced bandwidth
* Better performance

---

# Filtering and Sorting

REST APIs support query parameters.

## Filtering Example

```http
GET /products?category=electronics
```

---

## Sorting Example

```http
GET /products?sort=price
```

---

## Searching Example

```http
GET /products?search=laptop
```

---

# Error Handling

REST APIs return structured errors.

Example:

```json
{
  "error": "Invalid credentials"
}
```

Common practices:

* Meaningful messages
* Proper status codes
* Validation errors

---

# Rate Limiting

Rate limiting prevents API abuse.

Example:

```http
429 Too Many Requests
```

Common uses:

* Prevent spam
* Prevent DDoS attacks
* Protect server resources

---

# Caching in REST APIs

Caching improves performance.

Example:

```http
Cache-Control: max-age=3600
```

Benefits:

* Faster responses
* Reduced database load
* Better scalability

---

# REST API Best Practices

## Use Proper HTTP Methods

```text
GET → Fetch
POST → Create
PUT → Update
DELETE → Remove
```

---

## Use Meaningful URLs

Good:

```text
/api/users/1
```

Bad:

```text
/api/getUserData
```

---

## Use JSON Responses

JSON is the industry standard.

---

## Use Proper Status Codes

Example:

```text
201 Created
404 Not Found
```

---

## Secure APIs

Use:

* HTTPS
* Authentication
* Validation
* Rate limiting

---

# REST API Limitations

REST APIs also have limitations.

---

## Overfetching

Sometimes APIs return unnecessary data.

---

## Underfetching

Client may need multiple requests.

---

## Multiple Endpoints

Large systems may contain many endpoints.

---

## Stateless Overhead

Every request carries authentication data.

---

# REST vs SOAP

| Feature    | REST         | SOAP           |
| ---------- | ------------ | -------------- |
| Format     | JSON/XML     | XML            |
| Simplicity | Simple       | Complex        |
| Speed      | Faster       | Slower         |
| Protocol   | HTTP-based   | Multiple       |
| Popularity | Very Popular | Enterprise Use |

---

# REST vs GraphQL

| Feature       | REST     | GraphQL         |
| ------------- | -------- | --------------- |
| Endpoints     | Multiple | Single Endpoint |
| Data Fetching | Fixed    | Flexible        |
| Overfetching  | Possible | Reduced         |
| Complexity    | Simpler  | More Complex    |

---

# REST API in Node.js

Node.js can easily create REST APIs.

## Example Using Express.js

```javascript
import express from "express";

const app = express();

app.use(express.json());

app.get("/users", (req, res) => {
  res.json([
    {
      id: 1,
      name: "Deepak"
    }
  ]);
});

app.listen(3000);
```

---

# REST API Request Using Fetch

```javascript
fetch("https://api.example.com/users")
  .then(res => res.json())
  .then(data => console.log(data));
```

---

# Real-World Example

## E-Commerce Application

### REST API Usage

| Feature         | REST API Usage |
| --------------- | -------------- |
| Product Listing | GET /products  |
| Login           | POST /login    |
| Cart Management | POST /cart     |
| Checkout        | POST /checkout |
| Orders          | GET /orders    |
| User Profile    | GET /users/:id |

---

# HTTPS in REST APIs

REST APIs should use:

```text
HTTPS
```

HTTPS provides:

* Encryption
* Secure communication
* Data protection
* Authentication security

Example:

```text
https://api.example.com
```

---

# Common REST API Headers

| Header        | Example          |
| ------------- | ---------------- |
| Content-Type  | application/json |
| Authorization | Bearer token     |
| Accept        | application/json |
| Cache-Control | no-cache         |
| Origin        | frontend domain  |

---

# Interview Questions

## Q: What is REST API?

An architectural style for building web services using HTTP.

---

## Q: Why are REST APIs stateless?

Because each request contains all information needed to process it.

---

## Q: Difference between PUT and PATCH?

* PUT replaces entire resource
* PATCH partially updates resource

---

## Q: What is JSON in REST APIs?

A lightweight data format used for communication.

---

## Q: Why use HTTP status codes?

They indicate success or failure of requests.

---

## Q: What is API versioning?

Managing different API versions while maintaining compatibility.

---

## Q: Why use HTTPS in APIs?

To secure communication and encrypt data.

---

# Key Takeaway

REST APIs are fundamental to modern software development.

They enable:

* Frontend-backend communication
* Mobile app integration
* Third-party services
* Scalable systems
* Cloud-based architectures

REST APIs use:

* HTTP methods
* JSON data
* Stateless communication
* Resource-based URLs

Understanding REST APIs is essential for:

* Backend developers
* Frontend developers
* Full-stack engineers
* Mobile developers
* DevOps engineers

Modern applications heavily depend on RESTful communication.

✨ End of Notes
