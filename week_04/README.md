# Week 4: Loops and Iteration

**Big Idea:** AAP (Algorithms and Programming)

---

## Learning Objectives

By the end of this week, you should be able to:
- Write for loops to iterate a specific number of times
- Write while loops for condition-based iteration
- Use loop control statements (break, continue)
- Understand iteration as a fundamental algorithmic concept

---

## AP CSP Concepts

### AAP-2: Iteration (Loops)
Iteration is the repetition of a process. Loops allow you to execute code multiple times.

### For Loops
Use when you know how many times to repeat:

```python
# Repeat 5 times
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate over a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# Range with start, stop, step
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
```

### While Loops
Use when you don't know how many times to repeat:

```python
# Continue until condition is false
count = 0
while count < 5:
    print(count)
    count += 1

# Common pattern: input validation
password = ""
while password != "secret":
    password = input("Enter password: ")
```

### Loop Control
```python
# break - exit the loop immediately
for i in range(100):
    if i == 5:
        break  # Stop at 5
    print(i)

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)  # 0, 1, 3, 4
```

### Nested Loops
```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

---

## Practice Files

1. **loops.py** - For and while loop exercises

---

## AP-Style Practice Questions

### Question 1
How many times does "Hello" print?
```python
for i in range(3):
    for j in range(2):
        print("Hello")
```
- A) 2
- B) 3
- C) 5
- D) 6

<details>
<summary>Answer</summary>
D) 6 — The outer loop runs 3 times, inner loop runs 2 times. 3 × 2 = 6
</details>

### Question 2
What is the final value of `total`?
```python
total = 0
for i in range(1, 5):
    total += i
```
- A) 4
- B) 10
- C) 15
- D) 5

<details>
<summary>Answer</summary>
B) 10 — Adds 1 + 2 + 3 + 4 = 10 (range(1,5) is 1,2,3,4)
</details>

### Question 3
What does this code output?
```python
i = 1
while i < 10:
    i = i * 2
print(i)
```
- A) 8
- B) 10
- C) 16
- D) 32

<details>
<summary>Answer</summary>
C) 16 — i goes: 1→2→4→8→16. When i=16, the condition i<10 is false, so loop ends.
</details>

### Question 4
An algorithm requires checking each element in a list of n items. Which best describes its time complexity?
- A) The algorithm runs in constant time
- B) The algorithm runs in linear time
- C) The algorithm runs in quadratic time
- D) The algorithm cannot be analyzed

<details>
<summary>Answer</summary>
B) Linear time — Checking each element once requires n operations, which is linear.
</details>

---

## Key Takeaways

1. For loops are best when you know the number of iterations
2. While loops are best when you don't know when to stop
3. Be careful with infinite loops (while True without break)
4. Nested loops multiply iterations (outer × inner)
5. Iteration is fundamental to processing collections of data
