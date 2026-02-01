# Week 9: Functions and Procedural Abstraction

**Big Ideas:** AAP (Algorithms and Programming), CRD (Creative Development)

---

## Learning Objectives

By the end of this week, you should be able to:
- Define and call functions with parameters
- Understand return values vs printing
- Use procedural abstraction to manage complexity
- Document functions properly

---

## AP CSP Concepts

### AAP-3: Procedural Abstraction
A **procedure** (function) is a named group of instructions that can be reused.

**Abstraction** means hiding complexity - you can use a function without knowing how it works internally.

### Defining Functions
```python
# Function with no parameters
def greet():
    print("Hello!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Function with return value
def add(a, b):
    return a + b

# Function with default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"
```

### Parameters vs Arguments
- **Parameter**: Variable in function definition
- **Argument**: Actual value passed when calling

```python
def multiply(x, y):    # x and y are parameters
    return x * y

result = multiply(3, 4)  # 3 and 4 are arguments
```

### Return vs Print
```python
# Return - gives value back to caller
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)  # area = 15
print(area * 2)              # Can use the value

# Print - only displays, no value returned
def display_area(length, width):
    print(length * width)

result = display_area(5, 3)  # Prints 15, but result = None
```

### Scope
Variables inside functions are **local** - they only exist within that function.

```python
def my_function():
    local_var = 10  # Only exists inside function
    return local_var

# print(local_var)  # Error! Not defined outside function
```

### Why Use Functions?
1. **Reusability** - Write once, use many times
2. **Modularity** - Break complex problems into smaller pieces
3. **Readability** - Named functions explain what code does
4. **Maintainability** - Fix bugs in one place
5. **Abstraction** - Hide implementation details

---

## AP Pseudocode for Procedures

```
PROCEDURE name(param1, param2)
    instructions
    RETURN value

result ← name(arg1, arg2)
```

---

## Practice Files

1. **01_exceptions.py** - Error handling with try/except
2. **functions.py** - Function practice exercises

---

## AP-Style Practice Questions

### Question 1
```python
def mystery(a, b):
    a = a + b
    return a

x = 5
y = 3
result = mystery(x, y)
print(x, result)
```
What is printed?
- A) 8 8
- B) 5 8
- C) 5 5
- D) 8 5

<details>
<summary>Answer</summary>
B) 5 8 — x is not modified (passed by value); result gets the returned value 8
</details>

### Question 2
What is the benefit of procedural abstraction?
- A) It makes programs run faster
- B) It allows managing complexity by hiding implementation details
- C) It reduces the amount of memory used
- D) It eliminates the need for variables

<details>
<summary>Answer</summary>
B) It allows managing complexity by hiding implementation details
</details>

### Question 3
```python
def calculate(n):
    if n <= 1:
        return 1
    return n * calculate(n - 1)
```
What does `calculate(4)` return?
- A) 4
- B) 10
- C) 24
- D) 16

<details>
<summary>Answer</summary>
C) 24 — This is factorial: 4 × 3 × 2 × 1 = 24
</details>

### Question 4
A programmer writes a function to validate email addresses. Later, the validation rules change. What is the advantage of using a function?
- A) The change only needs to be made in one place
- B) The program will run faster
- C) Less memory is used
- D) The function automatically updates

<details>
<summary>Answer</summary>
A) The change only needs to be made in one place — This is a key benefit of modular code
</details>

---

## Key Takeaways

1. Functions encapsulate reusable code
2. Parameters make functions flexible
3. Return values allow functions to produce output for use elsewhere
4. Procedural abstraction hides complexity
5. Well-named functions make code self-documenting
