# Day 51 – OAuth Login

## 📜 What is OAuth?

**OAuth (Open Authorization)** is an authorization framework that allows users to log in to an application using another service (Google, GitHub, Facebook, etc.) **without sharing their password** with the application.

👉 User authenticates with a trusted provider
👉 Application receives permission to access user information
👉 Password is never exposed to the application

---

## 🧠 Why OAuth?

Traditional Login:

User → Username + Password → Application

Problems:

❌ Users must create new accounts
❌ Password management complexity
❌ Security risks if passwords are stored poorly

With OAuth:

User → Google/GitHub → Application

✔ Faster signup/login
✔ Better security
✔ No password storage needed

---

## 🔁 How OAuth Works

1️⃣ User clicks "Login with Google"

2️⃣ Application redirects user to OAuth Provider

3️⃣ User authenticates with provider

4️⃣ Provider asks for permission

5️⃣ Provider sends authorization code

6️⃣ Application exchanges code for access token

7️⃣ User logged in successfully

---

## 📦 Example – Login with Google

### Without OAuth

User creates account

Email + Password

Problems:

❌ Password reset functionality needed
❌ Credential storage required

---

### With OAuth

User clicks:

"Continue with Google"

Google handles authentication.

Application receives verified user information.

---

## ⚙ OAuth Authorization Flow

User
↓
Application
↓
OAuth Provider (Google)

Authorization Request
↓
User Login & Consent
↓
Authorization Code
↓
Access Token
↓
User Authenticated

---

## 🔄 OAuth Flow in Detail

### Step 1: Authorization Request

Application redirects user:

```text
https://accounts.google.com/o/oauth2/auth
```

User is sent to Google's login page.

---

### Step 2: User Authentication

User enters credentials directly on Google.

Application never sees the password.

---

### Step 3: User Consent

Google asks:

"Allow this app to access your profile?"

User chooses:

✔ Allow

OR

❌ Deny

---

### Step 4: Authorization Code

Google sends:

```text
Authorization Code
```

to the application.

---

### Step 5: Access Token Exchange

Application sends code to OAuth provider.

Provider returns:

```text
Access Token
```

---

### Step 6: Access Protected Resources

Application uses token to fetch:

✔ User profile

✔ Email

✔ Other permitted data

---

## 🧩 Key OAuth Components

| Component            | Purpose                |
| -------------------- | ---------------------- |
| Resource Owner       | User                   |
| Client               | Application            |
| Authorization Server | Google/GitHub          |
| Resource Server      | User data API          |
| Access Token         | Grants access          |
| Refresh Token        | Gets new access tokens |

---

## 📊 OAuth vs Traditional Login

| Feature                | Traditional Login | OAuth              |
| ---------------------- | ----------------- | ------------------ |
| Password Stored by App | Yes               | No                 |
| User Convenience       | Lower             | Higher             |
| Security               | Moderate          | Better             |
| Social Login           | No                | Yes                |
| Password Resets        | Required          | Usually Not Needed |

---

## 📦 Types of OAuth Tokens

### Access Token

Used to access APIs.

Example:

```text
Bearer eyJhbGciOi...
```

Characteristics:

✔ Short-lived

✔ Sent with API requests

---

### Refresh Token

Used to obtain a new access token.

Characteristics:

✔ Long-lived

✔ More secure storage required

---

## ⚠ Common OAuth Scopes

Scopes define permissions.

Examples:

```text
email
profile
openid
```

Examples:

✔ Read profile

✔ Read email

✔ Access calendar

---

## 🚀 OAuth + OpenID Connect (OIDC)

OAuth provides:

✔ Authorization

But not identity verification.

For authentication/login:

Use:

**OAuth + OpenID Connect (OIDC)**

OIDC adds:

✔ ID Token

✔ User identity information

This is what powers most "Login with Google" systems.

---

## 🔄 Token Lifecycle

User Login
↓
Access Token Issued
↓
Token Expires
↓
Refresh Token Used
↓
New Access Token Issued

---

## ⚙ Security Best Practices

✔ Use HTTPS

✔ Validate tokens

✔ Store tokens securely

✔ Use short-lived access tokens

✔ Implement token expiration

✔ Use PKCE for public clients

---

## 📦 Popular OAuth Providers

✔ Google

✔ GitHub

✔ Facebook

✔ Microsoft

✔ LinkedIn

---

## ⚠ Common Mistakes

❌ Storing access tokens insecurely

❌ Not validating token signatures

❌ Using long-lived access tokens

❌ Requesting unnecessary scopes

❌ Skipping HTTPS

❌ Exposing client secrets in frontend code

---

## 🛠 Example Flow – Login with Google

User clicks Login with Google
↓
Redirect to Google
↓
User authenticates
↓
User grants permission
↓
Authorization code returned
↓
Application exchanges code for token
↓
User logged in

---

## 🎯 Interview Questions

**Q: What is OAuth?**

An authorization framework that allows applications to access user resources without handling user passwords.

---

**Q: What is the difference between OAuth and Authentication?**

OAuth handles authorization (permissions), while authentication verifies identity.

---

**Q: What is an Access Token?**

A token used to access protected APIs on behalf of a user.

---

**Q: What is a Refresh Token?**

A token used to obtain a new access token when the current one expires.

---

**Q: What is the Authorization Code Flow?**

A secure OAuth flow where an authorization code is exchanged for an access token.

---

**Q: What is OpenID Connect (OIDC)?**

An authentication layer built on top of OAuth that provides user identity information.

---

**Q: Why is OAuth more secure than storing passwords?**

The application never handles the user's credentials directly and relies on trusted identity providers.

---

## ✅ Key Takeaway

OAuth enables:

✔ Secure third-party login

✔ Authorization without sharing passwords

✔ Better user experience

✔ Access control using tokens

When combined with **OpenID Connect (OIDC)**, it becomes the standard solution for modern **social login and authentication systems**.

✨ End of Day 51 – OAuth Login
