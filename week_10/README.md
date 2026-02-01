# Week 10: Libraries and APIs

**Big Ideas:** AAP (Algorithms and Programming), CRD (Creative Development)

---

## Learning Objectives

By the end of this week, you should be able to:
- Import and use Python libraries
- Understand what an API is
- Work with common libraries (random, datetime, requests)
- Recognize how libraries enable code reuse

---

## AP CSP Concepts

### CRD-2: Using Libraries
**Libraries** (also called modules or packages) are pre-written code that you can use in your programs.

Benefits:
- Don't reinvent the wheel
- Tested and optimized code
- Focus on your unique problem

### Importing Libraries
```python
# Import entire module
import random
value = random.randint(1, 10)

# Import specific functions
from random import randint, choice
value = randint(1, 10)

# Import with alias
import datetime as dt
today = dt.date.today()
```

### Common Standard Libraries

**random** - Random number generation
```python
import random
random.randint(1, 100)     # Random integer 1-100
random.choice([1, 2, 3])   # Random element from list
random.shuffle(my_list)    # Shuffle list in place
```

**datetime** - Date and time handling
```python
from datetime import datetime, date
now = datetime.now()
today = date.today()
```

**math** - Mathematical functions
```python
import math
math.sqrt(16)    # 4.0
math.pi          # 3.14159...
math.ceil(4.2)   # 5
math.floor(4.8)  # 4
```

**json** - JSON encoding/decoding
```python
import json
json.dumps(data)  # Python → JSON string
json.loads(text)  # JSON string → Python
```

### What is an API?
**API** (Application Programming Interface) defines how different software components interact.

- Library API: Functions you can call
- Web API: HTTP endpoints you can request

```python
# Example: Using a web API
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
```

### Documentation
Always check library documentation to learn:
- What functions are available
- What parameters they accept
- What they return
- Example usage

---

## Practice Files

1. **01_external_packages.py** - Working with libraries and APIs

---

## AP-Style Practice Questions

### Question 1
Which statement correctly imports the `randint` function from the `random` module?
- A) `import randint from random`
- B) `from random import randint`
- C) `import random.randint`
- D) `random import randint`

<details>
<summary>Answer</summary>
B) from random import randint
</details>

### Question 2
A programmer wants to use a library that validates email addresses. The library's documentation shows:
```
validate_email(email_string) → returns True if valid, False otherwise
```
This describes the library's:
- A) Source code
- B) License agreement
- C) API
- D) Installation process

<details>
<summary>Answer</summary>
C) API — The API defines how to use the library (function names, parameters, return values)
</details>

### Question 3
Why do programmers use libraries?
- A) Libraries make programs run faster
- B) Libraries reduce the need for testing
- C) Libraries allow reuse of existing, tested solutions
- D) Libraries are required by all programming languages

<details>
<summary>Answer</summary>
C) Libraries allow reuse of existing, tested solutions
</details>

### Question 4
```python
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
```
After this code runs, what is true about `numbers`?
- A) It contains the same elements in the same order
- B) It contains the same elements in a random order
- C) It is empty
- D) It contains new random numbers

<details>
<summary>Answer</summary>
B) It contains the same elements in a random order — shuffle rearranges in place
</details>

---

## Key Takeaways

1. Libraries provide pre-written, tested code
2. Use `import` to access library functionality
3. APIs define how to interact with software components
4. Documentation tells you how to use a library's API
5. Using libraries is a form of abstraction - you don't need to know internal details
