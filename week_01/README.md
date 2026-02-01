# Week 1: Variables, Data Types, and Expressions

**Big Idea:** AAP (Algorithms and Programming)

---

## Learning Objectives

By the end of this week, you should be able to:
- Declare and use variables in Python
- Understand different data types (int, float, str, bool)
- Write arithmetic and string expressions
- Use the assignment operator correctly

---

## AP CSP Concepts

### AAP-1: Variables and Assignments
- A **variable** is an abstraction that holds a value
- Variables have **names** (identifiers) and **values**
- The **assignment operator** (=) stores a value in a variable

```python
score = 100        # Integer
temperature = 98.6 # Float (decimal)
name = "Alice"     # String (text)
is_valid = True    # Boolean (True/False)
```

### AAP-2: Data Types
| Type | Description | Example |
|------|-------------|---------|
| `int` | Whole numbers | `42`, `-7`, `0` |
| `float` | Decimal numbers | `3.14`, `-0.5` |
| `str` | Text (strings) | `"Hello"`, `'World'` |
| `bool` | True or False | `True`, `False` |

### AAP-2: Arithmetic Operators
| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `6 * 7` | `42` |
| `/` | Division | `15 / 4` | `3.75` |
| `//` | Floor Division | `15 // 4` | `3` |
| `%` | Modulo (remainder) | `15 % 4` | `3` |
| `**` | Exponentiation | `2 ** 3` | `8` |

---

## Practice Files

1. **variables.py** - Basic variable declaration and usage
2. **arithmetic.py** - Mathematical operations and expressions

---

## AP-Style Practice Questions

### Question 1
What is stored in `x` after this code runs?
```python
x = 5
x = x + 3
x = x * 2
```
- A) 5
- B) 8
- C) 16
- D) 13

<details>
<summary>Answer</summary>
C) 16 — First x=5, then x=8, then x=16
</details>

### Question 2
Which of the following is NOT a valid variable name in Python?
- A) `my_variable`
- B) `myVariable`
- C) `2ndPlace`
- D) `_private`

<details>
<summary>Answer</summary>
C) 2ndPlace — Variable names cannot start with a number
</details>

### Question 3
What is the value of `result`?
```python
result = 17 % 5
```
- A) 3.4
- B) 3
- C) 2
- D) 12

<details>
<summary>Answer</summary>
C) 2 — The modulo operator returns the remainder. 17 ÷ 5 = 3 remainder 2
</details>

---

## Key Takeaways

1. Variables store data that can change during program execution
2. Python automatically determines the data type based on the value
3. Expressions combine values and operators to produce new values
4. The order of operations (PEMDAS) applies to Python arithmetic
