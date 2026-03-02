# Day 13 – API Versioning

## 🔢 What is API Versioning?

**API Versioning** is the practice of managing changes to an API  
without breaking existing clients.

As APIs evolve:

- New features are added
- Fields are modified
- Endpoints change
- Bugs are fixed

Versioning ensures:

👉 Backward compatibility  
👉 Smooth upgrades  
👉 Stable integrations  

---

## 🧠 Why API Versioning is Important

Without versioning:

❌ Existing clients break  
❌ Mobile apps stop working  
❌ Third-party integrations fail  
❌ Deployment becomes risky  

With versioning:

✔ Safe evolution  
✔ Controlled releases  
✔ Long-term maintainability  

---

## 📦 Example Problem

Initial API:

GET /users


Response:

```json
{
  "id": 1,
  "name": "Deepak"
}

Later requirement:

Add email field.

If response changes unexpectedly:

❌ Old clients may fail.

Solution:

Introduce new version.

🧩 Common Versioning Strategies
✅ 1️⃣ URL Versioning (Most Common)

Version included in URL.

Example:

/v1/users
/v2/users

Pros:

✔ Clear
✔ Simple
✔ Widely used

Cons:

❌ URL changes

✅ 2️⃣ Header Versioning

Version passed via custom header.

Example:

GET /users
API-Version: 2

Pros:

✔ Clean URLs

Cons:

❌ Harder to test manually

Pros:

✔ Clean URLs

Cons:

❌ Harder to test manually

/users?version=2

Less common.

✅ 4️⃣ Content Negotiation (Advanced)

Version specified via Accept header.

Example:

Accept: application/vnd.myapp.v2+json

Used in enterprise APIs.

🚀 Best Practice Recommendation

For most backend systems:

👉 Use URL versioning

Example:

/api/v1/users
/api/v2/users

🔄 Backward Compatibility

When designing new version:

✔ Do not remove existing fields
✔ Add new optional fields
✔ Avoid breaking response structure
✔ Deprecate gradually

🛠 Example Version Evolution
Version 1

GET /api/v1/users

Response:

{
  "id": 1,
  "name": "Deepak"
}

Version 2

GET /api/v2/users

Response:

{
  "id": 1,
  "name": "Deepak",
  "email": "deepak@email.com"
}

⚠ Deprecation Strategy

When retiring old version:

✔ Announce deprecation
✔ Provide migration guide
✔ Set sunset date
✔ Monitor usage

📊 Semantic Versioning (Related Concept)

Format:

MAJOR.MINOR.PATCH

Example:

2.1.0

MAJOR → Breaking changes

MINOR → New features

PATCH → Bug fixes

✅ Key Takeaway

API versioning allows:

✔ Safe evolution
✔ Stable integrations
✔ Professional backend design

Design APIs assuming they will evolve.

✨ End of Day 13