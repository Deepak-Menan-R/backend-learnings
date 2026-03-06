# Day 17 – Load Balancing

## What is Load Balancing?

**Load balancing** is the process of distributing incoming network traffic across multiple servers to ensure no single server becomes overloaded.

Instead of sending all requests to one server, a **load balancer** spreads requests evenly across multiple servers.

Goal:

- Improve scalability
- Increase reliability
- Prevent server overload
- Improve response times

---

## Why Load Balancing is Important

Without load balancing:

- One server handles all requests  
- Server overload  
- Poor performance  
- Single point of failure  

With load balancing:

- Better traffic distribution  
- Improved performance  
- High availability  
- Fault tolerance  

---

## Basic Architecture

Client → Load Balancer → Application Servers → Database

Example:

       Client
          |
    Load Balancer
     /     |     \
 Server1 Server2 Server3

 
The load balancer decides **which server handles each request**.

---

## Benefits of Load Balancing

- Distributes traffic evenly  
- Prevents server overload  
- Enables horizontal scaling  
- Improves fault tolerance  
- Maintains system availability  

---

## Load Balancing Algorithms

### Round Robin

Requests are distributed **sequentially**.

Example:

Request1 → Server1
Request2 → Server2
Request3 → Server3
Request4 → Server1


Simple and widely used.

---

### Least Connections

Request goes to server with **fewest active connections**.

Useful when:

- Some requests take longer than others.

---

### IP Hash

Server selection based on **client IP address**.

Benefits:

- Same client always reaches same server.

Used for **session persistence**.

---

### Weighted Round Robin

Servers have different capacities.

Example:

Server1 weight = 3
Server2 weight = 1


Server1 receives more traffic.

---

## Types of Load Balancers

### Layer 4 Load Balancer

Operates at **Transport Layer** (TCP/UDP).

Uses:

- IP address
- Port number

Example tools:

- AWS NLB
- HAProxy

---

### Layer 7 Load Balancer

Operates at **Application Layer (HTTP)**.

Can route based on:

- URL
- Headers
- Cookies

Example tools:

- Nginx
- AWS ALB

---

## Health Checks

Load balancers perform **health checks** to determine if a server is healthy.

Example:

GET /health


If a server fails health checks:

- Removed from traffic routing.

---

## Sticky Sessions (Session Persistence)

Sometimes the same client must always connect to the same server.

Example:

Client A → Server2


This ensures session data remains consistent.

But modern systems prefer:

- Stateless APIs  
- Shared session stores (Redis)

---

## Single Point of Failure

If the load balancer itself fails:

- Entire system becomes unavailable.

Solution:

- Multiple load balancers  
- Failover systems  
- DNS load balancing

---

## Real-World Load Balancers

Popular solutions:

- Nginx
- HAProxy
- AWS Application Load Balancer
- Google Cloud Load Balancer
- Cloudflare Load Balancer

---

## Common Mistakes

- No health checks  
- Uneven server capacity handling  
- Sticky sessions without need  
- Single load balancer instance  

---

## Interview Questions

**Q: What is load balancing?**

Distributing incoming traffic across multiple servers.

---

**Q: Why is load balancing used?**

To improve scalability, reliability, and performance.

---

**Q: Round Robin vs Least Connections?**

Round Robin → Equal distribution  
Least Connections → Based on server load

---

**Q: Layer 4 vs Layer 7 load balancing?**

Layer 4 → Network level  
Layer 7 → Application level

---

## Key Takeaway

Load balancing ensures:

- High availability  
- Scalability  
- Fault tolerance  
- Better performance  

It is a core concept in designing scalable backend systems.

End of Day 17