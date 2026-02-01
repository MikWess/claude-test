# Week 6: Algorithms - Searching and Sorting

**Big Idea:** AAP (Algorithms and Programming)

---

## Learning Objectives

By the end of this week, you should be able to:
- Implement linear search and binary search
- Understand basic sorting algorithms
- Compare algorithm efficiency
- Describe algorithms using pseudocode

---

## AP CSP Concepts

### AAP-2: Algorithms
An **algorithm** is a finite set of instructions that accomplish a task.

### Linear Search
Checks each element one by one until the target is found.

```python
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # Found at index i
    return -1  # Not found
```

**Efficiency:** O(n) - must check up to n elements

### Binary Search
Requires a **sorted** list. Eliminates half the remaining elements each step.

```python
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found
```

**Efficiency:** O(log n) - much faster for large lists!

### Comparing Searches
| List Size | Linear (worst) | Binary (worst) |
|-----------|----------------|----------------|
| 8 | 8 checks | 3 checks |
| 1,000 | 1,000 checks | 10 checks |
| 1,000,000 | 1,000,000 checks | 20 checks |

### Sorting Algorithms

**Selection Sort** - Find minimum, swap to front, repeat
```python
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
```

**Bubble Sort** - Compare adjacent pairs, swap if out of order, repeat
```python
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
```

---

## AP Pseudocode for Binary Search

```
PROCEDURE BinarySearch(list, target)
    low ← 1
    high ← LENGTH(list)
    REPEAT UNTIL low > high
        mid ← (low + high) / 2
        IF list[mid] = target
            RETURN mid
        ELSE IF list[mid] < target
            low ← mid + 1
        ELSE
            high ← mid - 1
    RETURN -1
```

---

## Practice Files

1. **searching.py** - Linear and binary search implementations
2. **sorting.py** - Sorting algorithm implementations

---

## AP-Style Practice Questions

### Question 1
A sorted list contains 1000 elements. What is the maximum number of comparisons needed for binary search?
- A) 1000
- B) 500
- C) 10
- D) 100

<details>
<summary>Answer</summary>
C) 10 — Binary search takes at most log₂(1000) ≈ 10 comparisons
</details>

### Question 2
When is linear search preferred over binary search?
- A) When the list is very large
- B) When the list is unsorted
- C) When you need the fastest search
- D) When the list contains duplicates

<details>
<summary>Answer</summary>
B) When the list is unsorted — Binary search requires a sorted list
</details>

### Question 3
In selection sort, after 3 passes through a list of 10 elements, how many elements are guaranteed to be in their final positions?
- A) 0
- B) 3
- C) 7
- D) 10

<details>
<summary>Answer</summary>
B) 3 — Each pass places one element in its final position
</details>

### Question 4
Which best describes the relationship between problem size and execution time for binary search?
- A) Constant - time doesn't change with size
- B) Linear - time increases proportionally with size
- C) Logarithmic - time increases slowly with size
- D) Quadratic - time increases with the square of size

<details>
<summary>Answer</summary>
C) Logarithmic — Binary search has O(log n) time complexity
</details>

---

## Key Takeaways

1. Linear search works on any list but is slow for large lists
2. Binary search is much faster but requires a sorted list
3. Sorting algorithms have different efficiencies
4. Understanding algorithm efficiency is essential for solving problems at scale
5. The AP exam focuses on understanding, not memorizing algorithms
