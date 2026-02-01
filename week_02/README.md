# Week 2: Input/Output and Data Representation

**Big Ideas:** AAP (Algorithms and Programming), DAT (Data)

---

## Learning Objectives

By the end of this week, you should be able to:
- Get user input and display output
- Convert between data types
- Understand how data is represented in computers (binary)
- Work with string operations

---

## AP CSP Concepts

### AAP-1: Input and Output
Programs interact with users through **input** (receiving data) and **output** (displaying results).

```python
# Input - getting data from user
name = input("What is your name? ")
age = int(input("What is your age? "))

# Output - displaying data
print("Hello,", name)
print(f"You are {age} years old")
```

### DAT-1: Data Representation (Binary)
Computers store ALL data as **binary** (0s and 1s).

| Decimal | Binary | Bits |
|---------|--------|------|
| 0 | 0 | 1 |
| 1 | 1 | 1 |
| 5 | 101 | 3 |
| 10 | 1010 | 4 |
| 255 | 11111111 | 8 |

**Key Terms:**
- **Bit**: Single binary digit (0 or 1)
- **Byte**: 8 bits (can represent 0-255)
- **Overflow**: When a value exceeds the maximum representable number

```python
# Converting to/from binary in Python
bin(10)      # '0b1010' - decimal to binary
int('1010', 2)  # 10 - binary to decimal
```

### DAT-1: Text Representation (ASCII/Unicode)
Characters are stored as numbers:
- `'A'` = 65
- `'a'` = 97
- `'0'` = 48

```python
ord('A')    # 65 - character to number
chr(65)     # 'A' - number to character
```

### Type Conversion
```python
# String to number
x = int("42")      # 42 (integer)
y = float("3.14")  # 3.14 (float)

# Number to string
s = str(100)       # "100"

# Float to int (truncates)
n = int(3.9)       # 3 (not rounded!)
```

---

## Practice Files

1. **input_output.py** - User interaction practice
2. **data_representation.py** - Binary and type conversion exercises

---

## AP-Style Practice Questions

### Question 1
What is displayed when this code runs?
```python
x = input("Enter a number: ")  # User enters: 5
print(x * 3)
```
- A) 15
- B) 555
- C) 8
- D) Error

<details>
<summary>Answer</summary>
B) 555 — input() returns a string, so "5" * 3 = "555" (string repetition)
</details>

### Question 2
How many bits are needed to represent the number 100 in binary?
- A) 5
- B) 6
- C) 7
- D) 8

<details>
<summary>Answer</summary>
C) 7 — 100 in binary is 1100100, which requires 7 bits
</details>

### Question 3
What is the decimal value of binary 1101?
- A) 11
- B) 13
- C) 14
- D) 15

<details>
<summary>Answer</summary>
B) 13 — (1×8) + (1×4) + (0×2) + (1×1) = 8 + 4 + 0 + 1 = 13
</details>

### Question 4
In a system using 8 bits to represent unsigned integers, what happens when you try to store 300?
- A) The value is stored correctly
- B) An overflow error occurs
- C) The value wraps around to a smaller number
- D) The computer automatically uses more bits

<details>
<summary>Answer</summary>
C) The value wraps around — 8 bits can only represent 0-255, so 300 would cause overflow
</details>

---

## Key Takeaways

1. `input()` always returns a string - convert if you need a number
2. All data in computers is ultimately stored as binary (bits)
3. Understanding binary helps explain limitations like overflow errors
4. ASCII/Unicode maps characters to numbers for storage
