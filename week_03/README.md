# Week 3: Conditionals (Selection)

**Big Idea:** AAP (Algorithms and Programming)

---

## Learning Objectives

By the end of this week, you should be able to:
- Write conditional statements using if/elif/else
- Use comparison operators (==, !=, <, >, <=, >=)
- Combine conditions with logical operators (and, or, not)
- Understand how selection affects program flow

---

## AP CSP Concepts

### AAP-2: Selection (Conditional Statements)
Selection determines which parts of an algorithm are executed based on a condition.

```python
# Basic if statement
if temperature > 100:
    print("It's hot!")

# if-else
if score >= 60:
    print("Pass")
else:
    print("Fail")

# if-elif-else
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

### Comparison Operators
| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `<` | Less than | `x < 5` |
| `>` | Greater than | `x > 5` |
| `<=` | Less than or equal | `x <= 5` |
| `>=` | Greater than or equal | `x >= 5` |

### Logical Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Both must be true | `x > 0 and x < 10` |
| `or` | At least one must be true | `x < 0 or x > 100` |
| `not` | Inverts the condition | `not is_done` |

### Nested Conditionals
```python
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("Too young to drive")
```

---

## Practice Files

1. **01_conditionals.py** - If statements and comparison operators

---

## AP-Style Practice Questions

### Question 1
What is displayed when this code runs?
```python
x = 7
if x > 10:
    print("A")
elif x > 5:
    print("B")
elif x > 0:
    print("C")
else:
    print("D")
```
- A) A
- B) B
- C) C
- D) D

<details>
<summary>Answer</summary>
B) B — x is 7, which is > 5 but not > 10, so "B" prints. Once a condition is true, the rest are skipped.
</details>

### Question 2
Which expression evaluates to True?
```python
a = 5
b = 10
c = 5
```
- A) `a == b and b == c`
- B) `a == b or a == c`
- C) `a > b and a < c`
- D) `not (a == c)`

<details>
<summary>Answer</summary>
B) a == b or a == c — a == c is True, so the or expression is True
</details>

### Question 3
What is the value of `result`?
```python
x = 15
result = "even" if x % 2 == 0 else "odd"
```
- A) "even"
- B) "odd"
- C) True
- D) Error

<details>
<summary>Answer</summary>
B) "odd" — 15 % 2 = 1, which is not 0, so the condition is False and "odd" is assigned
</details>

---

## Key Takeaways

1. Selection (if statements) controls which code blocks execute
2. Conditions evaluate to True or False (Boolean values)
3. Use elif to check multiple conditions in sequence
4. Logical operators combine multiple conditions
5. The order of elif conditions matters - first true condition wins
