# Week 5: Lists and Data Collections

**Big Ideas:** DAT (Data), AAP (Algorithms and Programming)

---

## Learning Objectives

By the end of this week, you should be able to:
- Create and manipulate lists
- Access list elements using indices
- Use list methods (append, insert, remove, pop)
- Understand lists as abstractions for managing collections

---

## AP CSP Concepts

### DAT-2: Using Data
Lists (also called arrays in AP pseudocode) store ordered collections of data.

### AAP-1: Lists as Abstractions
```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]
empty = []
```

### Indexing (0-based)
```python
colors = ["red", "green", "blue", "yellow"]
#          0       1        2        3

colors[0]   # "red" (first element)
colors[2]   # "blue" (third element)
colors[-1]  # "yellow" (last element)
colors[-2]  # "blue" (second to last)
```

### List Operations
```python
numbers = [1, 2, 3]

# Add elements
numbers.append(4)      # [1, 2, 3, 4]
numbers.insert(0, 0)   # [0, 1, 2, 3, 4]

# Remove elements
numbers.remove(2)      # [0, 1, 3, 4]
last = numbers.pop()   # [0, 1, 3], last = 4

# Modify elements
numbers[0] = 10        # [10, 1, 3]

# Length
len(numbers)           # 3
```

### Iterating Over Lists
```python
# Using for loop (recommended)
for item in my_list:
    print(item)

# Using index
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")
```

### List Slicing
```python
numbers = [0, 1, 2, 3, 4, 5]

numbers[1:4]   # [1, 2, 3] (index 1 to 3)
numbers[:3]    # [0, 1, 2] (first 3)
numbers[3:]    # [3, 4, 5] (from index 3)
numbers[::2]   # [0, 2, 4] (every other)
```

---

## AP CSP: Lists in Pseudocode

The AP exam uses this pseudocode notation:
```
list ← [1, 2, 3]     // Create list
list[1]               // Access element (1-indexed on AP exam!)
APPEND(list, value)   // Add to end
INSERT(list, i, val)  // Insert at position
REMOVE(list, i)       // Remove at position
LENGTH(list)          // Get length
```

**Important:** AP pseudocode uses 1-based indexing! Python uses 0-based.

---

## Practice Files

1. **01_lists.py** - List creation and manipulation
2. **02_dictionaries.py** - Key-value data structures

---

## AP-Style Practice Questions

### Question 1
Given the list `nums = [10, 20, 30, 40, 50]`, what is `nums[2]`?
- A) 10
- B) 20
- C) 30
- D) 40

<details>
<summary>Answer</summary>
C) 30 — Index 2 is the third element (0-based indexing)
</details>

### Question 2
What is the result after executing this code?
```python
data = [1, 2, 3]
data.append(4)
data.pop(0)
```
- A) [1, 2, 3, 4]
- B) [2, 3, 4]
- C) [1, 2, 3]
- D) [2, 3]

<details>
<summary>Answer</summary>
B) [2, 3, 4] — append(4) adds 4, then pop(0) removes the first element
</details>

### Question 3
A programmer wants to find the average of all values in a list. Which approach is correct?

```
A) total = sum(list) / len(list)
B) average = list[0] + list[len(list)-1] / 2
C) Loop through and add each element, then divide by count
D) Both A and C are correct
```

<details>
<summary>Answer</summary>
D) Both A and C — Both sum(list)/len(list) and looping are valid approaches
</details>

### Question 4
Which code correctly doubles every element in a list?
```python
# Option A
for item in nums:
    item = item * 2

# Option B
for i in range(len(nums)):
    nums[i] = nums[i] * 2
```
- A) Option A only
- B) Option B only
- C) Both work
- D) Neither works

<details>
<summary>Answer</summary>
B) Option B only — Option A creates a new variable; it doesn't modify the list
</details>

---

## Key Takeaways

1. Lists store ordered, mutable collections of data
2. Indexing starts at 0 in Python (but 1 on AP pseudocode)
3. Lists can be modified: add, remove, update elements
4. Use loops to process all elements in a list
5. Lists are fundamental for managing collections of data
