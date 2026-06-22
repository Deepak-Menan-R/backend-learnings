# Day 53 – Queues

## 📜 What is a Queue?

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

This means:

✔ The first element added is the first element removed.

Just like a queue of people waiting at a ticket counter:

```text
Front                     Rear
 ↓                         ↓

[A] [B] [C] [D]

A leaves first
D leaves last
```

---

## 🧠 Why Queues?

Queues are used whenever tasks need to be processed in the same order they arrive.

Examples:

✔ Print jobs

✔ Customer support tickets

✔ Task scheduling

✔ Message processing

✔ Network packet handling

✔ Request management

---

## 🔁 FIFO Principle

FIFO means:

```text
First In → First Out
```

Example:

```text
Enqueue A
Enqueue B
Enqueue C

Queue:
[A] [B] [C]
```

Removing elements:

```text
Dequeue → A
Dequeue → B
Dequeue → C
```

Elements leave in the same order they entered.

---

## 📦 Queue Operations

### Enqueue

Adds an element to the rear.

```text
Queue:

[A] [B]

Enqueue(C)

[A] [B] [C]
```

---

### Dequeue

Removes an element from the front.

```text
Queue:

[A] [B] [C]

Dequeue()

[B] [C]
```

---

### Peek / Front

Returns front element without removing it.

```text
Queue:

[A] [B] [C]

Peek()

A
```

---

### isEmpty

Checks whether queue contains elements.

```javascript
queue.length === 0
```

---

### Size

Returns number of elements.

```text
[A] [B] [C]

Size = 3
```

---

## ⚙ Queue Flow

```text
Enqueue(A)
↓
[A]

Enqueue(B)
↓
[A][B]

Enqueue(C)
↓
[A][B][C]

Dequeue()
↓
[B][C]
```

---

## 🔄 Queue Visualization

```text
Front               Rear
 ↓                   ↓

[A] [B] [C] [D]

Dequeue()

Front          Rear
 ↓              ↓

[B] [C] [D]
```

---

## 📦 Queue Terminology

| Term    | Meaning            |
| ------- | ------------------ |
| Front   | First element      |
| Rear    | Last element       |
| Enqueue | Insert element     |
| Dequeue | Remove element     |
| FIFO    | First In First Out |
| Peek    | View front element |

---

## 🧩 Real-Life Example

### Ticket Counter

People arrive:

```text
A
B
C
D
```

Queue:

```text
Front

[A] [B] [C] [D]

Rear
```

Service order:

```text
A
B
C
D
```

Nobody can skip ahead.

---

## ⚙ Queue Using Array

### JavaScript Example

```javascript
const queue = [];

queue.push("A"); // Enqueue
queue.push("B");
queue.push("C");

console.log(queue);

queue.shift(); // Dequeue

console.log(queue);
```

Output:

```text
[A, B, C]

[B, C]
```

---

## ⚙ Queue Class Implementation

```javascript
class Queue {
  constructor() {
    this.items = [];
  }

  enqueue(item) {
    this.items.push(item);
  }

  dequeue() {
    return this.items.shift();
  }

  peek() {
    return this.items[0];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }
}
```

---

## 📊 Time Complexity (Array-Based)

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Peek      | O(1)       |
| isEmpty   | O(1)       |
| Size      | O(1)       |
| Dequeue   | O(n)       |

---

## ⚠ Why is Dequeue O(n)?

Arrays shift all remaining elements left.

Example:

```text
[A] [B] [C] [D]

Remove A

[B] [C] [D]
```

Every element moves one position.

---

## 🚀 Optimized Queue Using Linked List

Linked lists allow:

✔ O(1) enqueue

✔ O(1) dequeue

Structure:

```text
Front
 ↓

A → B → C → D

             ↑
           Rear
```

---

## 📦 Queue Using Linked List

### Node Structure

```javascript
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
```

---

### Queue Structure

```javascript
class Queue {
  constructor() {
    this.front = null;
    this.rear = null;
  }

  enqueue(value) {
    const node = new Node(value);

    if (!this.rear) {
      this.front = node;
      this.rear = node;
      return;
    }

    this.rear.next = node;
    this.rear = node;
  }

  dequeue() {
    if (!this.front) return null;

    const value = this.front.value;
    this.front = this.front.next;

    if (!this.front) {
      this.rear = null;
    }

    return value;
  }
}
```

---

## 📊 Time Complexity (Linked List Queue)

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Peek      | O(1)       |
| Size      | O(1)*      |

* If size is maintained separately.

---

## 🔄 Queue Example

Operations:

```text
Enqueue(10)
Enqueue(20)
Enqueue(30)
```

Queue:

```text
Front

[10] [20] [30]

Rear
```

---

Remove:

```text
Dequeue()
```

Result:

```text
20 30
```

Removed:

```text
10
```

---

## 📦 Types of Queues

### Simple Queue

Standard FIFO queue.

```text
A → B → C
```

---

### Circular Queue

Last position connects back to first.

```text
[A][B][C][D]
 ↑         ↓
 └─────────┘
```

Used to efficiently reuse memory.

---

### Priority Queue

Elements are removed based on priority.

Example:

```text
Task A (Priority 1)
Task B (Priority 5)
Task C (Priority 3)
```

Processing order:

```text
B
C
A
```

Not FIFO.

---

### Double-Ended Queue (Deque)

Insertion and deletion from both ends.

```text
Front ←→ Rear
```

Supports:

✔ Add front

✔ Remove front

✔ Add rear

✔ Remove rear

---

## 📦 Queue Applications

### CPU Scheduling

Processes wait in queue.

```text
P1 → P2 → P3
```

---

### Print Queue

Print jobs processed in order.

```text
Job1
Job2
Job3
```

---

### Web Server Requests

Incoming requests wait in queue.

```text
Request1
Request2
Request3
```

---

### Messaging Systems

Examples:

✔ RabbitMQ

✔ Kafka Consumers

✔ AWS SQS

Messages processed sequentially.

---

### BFS Traversal

Breadth-First Search uses queues.

```text
Visit Node
↓
Add neighbors
↓
Process neighbors
```

---

## 🌳 BFS Example

Tree:

```text
      A
     / \
    B   C
   / \
  D   E
```

Traversal:

```text
A
B
C
D
E
```

Queue Flow:

```text
[A]

Remove A
Add B,C

[B,C]

Remove B
Add D,E

[C,D,E]
```

---

## ⚠ Queue Overflow

Occurs when queue is full.

Example:

```text
Capacity = 3

[A][B][C]

Enqueue(D)
```

Result:

```text
Overflow
```

---

## ⚠ Queue Underflow

Occurs when removing from empty queue.

```text
Queue = []

Dequeue()
```

Result:

```text
Underflow
```

---

## 🔐 Best Practices

✔ Use linked lists for frequent dequeues

✔ Validate empty queue before removal

✔ Maintain queue size separately

✔ Use circular queues for fixed-size buffers

✔ Use priority queues when order matters by importance

---

## ⚠ Common Mistakes

❌ Removing from rear

❌ Forgetting FIFO behavior

❌ Dequeuing empty queue

❌ Using array shift() heavily for large queues

❌ Not updating front/rear pointers

---

## 🛠 Example Flow – Customer Support System

```text
Customer 1 creates ticket
↓
Customer 2 creates ticket
↓
Customer 3 creates ticket
↓
Queue formed
↓
Agent handles Customer 1
↓
Agent handles Customer 2
↓
Agent handles Customer 3
```

FIFO ensures fairness.

---

## 🎯 Interview Questions

### Q: What is a Queue?

A linear data structure that follows FIFO (First In, First Out).

---

### Q: What is Enqueue?

Adding an element to the rear of the queue.

---

### Q: What is Dequeue?

Removing an element from the front of the queue.

---

### Q: Why is Queue FIFO?

Because the first inserted element is removed first.

---

### Q: What is the difference between Stack and Queue?

| Stack                   | Queue                    |
| ----------------------- | ------------------------ |
| LIFO                    | FIFO                     |
| Push/Pop                | Enqueue/Dequeue          |
| Last item removed first | First item removed first |

---

### Q: What is a Circular Queue?

A queue where the last position connects back to the first position.

---

### Q: What is a Priority Queue?

A queue where elements are processed based on priority instead of insertion order.

---

### Q: Which algorithm commonly uses queues?

Breadth-First Search (BFS).

---

## ✅ Key Takeaway

Queues are a fundamental data structure that follow the **FIFO (First In, First Out)** principle.

They are widely used for:

✔ Task scheduling

✔ Request processing

✔ BFS traversal

✔ Messaging systems

✔ Print queues

✔ Real-time data processing

Understanding queues is essential because many backend systems, operating systems, and distributed applications rely heavily on queue-based processing.

✨ End of Day 53 – Queues
