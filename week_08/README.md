# Week 8: Algorithm Efficiency and Analysis

**Big Idea:** AAP (Algorithms and Programming)

---

## Learning Objectives

By the end of this week, you should be able to:
- Understand "reasonable" vs "unreasonable" time algorithms
- Recognize common time complexities
- Analyze simple algorithms for efficiency
- Understand why efficiency matters at scale

---

## AP CSP Concepts

### AAP-4: Algorithm Efficiency
Not all algorithms that solve a problem are equally efficient.

### Time Complexity Basics
| Complexity | Name | Example | 1000 items |
|------------|------|---------|------------|
| O(1) | Constant | Array access | 1 operation |
| O(log n) | Logarithmic | Binary search | ~10 operations |
| O(n) | Linear | Linear search | 1,000 operations |
| O(n log n) | Log-linear | Good sorting | ~10,000 operations |
| O(n²) | Quadratic | Nested loops | 1,000,000 operations |
| O(2ⁿ) | Exponential | Some recursion | Impossible! |

### Reasonable vs Unreasonable Time
**Reasonable (Polynomial):** O(1), O(n), O(n²), O(n³)
- Can be solved in a practical amount of time

**Unreasonable (Exponential/Factorial):** O(2ⁿ), O(n!)
- Becomes impractical very quickly
- Often requires approximation algorithms

### Example: Why Efficiency Matters

Finding an item in a list of 1 billion items:
- **Linear Search O(n):** Up to 1 billion comparisons
- **Binary Search O(log n):** At most 30 comparisons!

### Identifying Time Complexity

```python
# O(1) - Constant
def get_first(lst):
    return lst[0]

# O(n) - Linear
def find_max(lst):
    max_val = lst[0]
    for item in lst:      # Loop runs n times
        if item > max_val:
            max_val = item
    return max_val

# O(n²) - Quadratic
def find_duplicates(lst):
    for i in range(len(lst)):        # Outer: n times
        for j in range(len(lst)):    # Inner: n times
            if i != j and lst[i] == lst[j]:
                return True
    return False
```

### Heuristics and Approximations
When a problem has no efficient solution:
- Use **heuristics** (rules of thumb)
- Accept **approximate** solutions
- Example: Traveling Salesman Problem

---

## Practice Files

1. **efficiency.py** - Analyzing and comparing algorithm efficiency

---

## AP-Style Practice Questions

### Question 1
Which algorithm efficiency would be considered "unreasonable"?
- A) O(n)
- B) O(n²)
- C) O(n³)
- D) O(2ⁿ)

<details>
<summary>Answer</summary>
D) O(2ⁿ) — Exponential time is unreasonable; it grows too fast
</details>

### Question 2
An algorithm takes 1 second to process 1000 items. If it has O(n²) complexity, approximately how long for 2000 items?
- A) 2 seconds
- B) 4 seconds
- C) 8 seconds
- D) 1000 seconds

<details>
<summary>Answer</summary>
B) 4 seconds — O(n²) means doubling input quadruples time: (2000/1000)² = 4
</details>

### Question 3
```python
def mystery(n):
    count = 0
    i = n
    while i > 1:
        i = i // 2
        count += 1
    return count
```
What is the time complexity of this function?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

<details>
<summary>Answer</summary>
B) O(log n) — The loop halves i each time, so it runs log₂(n) times
</details>

### Question 4
A social network has 1 million users. An algorithm checks if any two users are friends by comparing all pairs. How many comparisons?
- A) 1 million
- B) 2 million
- C) About 500 billion
- D) 1 trillion

<details>
<summary>Answer</summary>
C) About 500 billion — n(n-1)/2 pairs ≈ 500 billion for n = 1 million
</details>

### Question 5
The Traveling Salesman Problem (finding shortest route through n cities) has no known polynomial-time solution. What approach would be reasonable for 100 cities?
- A) Check all possible routes
- B) Use a heuristic that finds a good (not perfect) solution
- C) Reduce the number of cities
- D) It's impossible to solve

<details>
<summary>Answer</summary>
B) Use a heuristic — For intractable problems, approximation algorithms give good solutions in reasonable time
</details>

---

## Key Takeaways

1. Algorithm efficiency matters as data grows larger
2. O(n²) vs O(n) can mean hours vs seconds
3. Exponential algorithms become impractical very quickly
4. Some problems have no efficient solution - use approximations
5. The AP exam focuses on understanding, not calculating complexity
