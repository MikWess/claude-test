"""
Week 8: Algorithm Efficiency
============================
Big Idea: AAP (Algorithms and Programming)

Understanding and analyzing algorithm efficiency.
"""

import time
import random

# =============================================================================
# Timing Helper
# =============================================================================

def time_function(func, *args):
    """Measure execution time of a function."""
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


# =============================================================================
# O(1) - Constant Time
# =============================================================================

def constant_time_example(lst):
    """
    O(1) - Always takes the same time regardless of list size.
    Accessing by index is constant time.
    """
    if len(lst) > 0:
        return lst[0], lst[-1]
    return None, None


# =============================================================================
# O(n) - Linear Time
# =============================================================================

def linear_time_example(lst):
    """
    O(n) - Time grows linearly with input size.
    Must look at each element once.
    """
    total = 0
    for item in lst:
        total += item
    return total


# =============================================================================
# O(n²) - Quadratic Time
# =============================================================================

def quadratic_time_example(lst):
    """
    O(n²) - Nested loops over the same data.
    Time grows with the square of input size.
    """
    pairs = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            pairs.append((lst[i], lst[j]))
    return len(pairs)


# =============================================================================
# TODO: Exercise 1 - Identify Complexity
# =============================================================================

def mystery_1(n):
    """What is the time complexity?"""
    count = 0
    for i in range(n):
        count += 1
    return count
    # Answer: ___


def mystery_2(n):
    """What is the time complexity?"""
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count
    # Answer: ___


def mystery_3(n):
    """What is the time complexity?"""
    count = 0
    i = n
    while i > 1:
        i = i // 2
        count += 1
    return count
    # Answer: ___


def mystery_4(n):
    """What is the time complexity?"""
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    return count
    # Answer: ___


# =============================================================================
# TODO: Exercise 2 - Compare Algorithms
# =============================================================================

def compare_linear_vs_quadratic():
    """
    Compare O(n) vs O(n²) algorithms on increasing input sizes.

    Create lists of sizes: 100, 500, 1000, 2000, 5000
    Time both linear and quadratic functions
    Print results in a table
    """
    sizes = [100, 500, 1000, 2000, 5000]

    print("Comparing O(n) vs O(n²)")
    print("=" * 50)
    print(f"{'Size':<10} {'O(n) time':<15} {'O(n²) time':<15}")
    print("-" * 50)

    for size in sizes:
        lst = list(range(size))

        # TODO: Time both functions
        # _, linear_time = time_function(linear_time_example, lst)
        # _, quad_time = time_function(quadratic_time_example, lst)
        # print(f"{size:<10} {linear_time:<15.6f} {quad_time:<15.6f}")
        pass


# =============================================================================
# TODO: Exercise 3 - Optimize an Algorithm
# =============================================================================

def find_duplicates_slow(lst):
    """
    O(n²) - Check every pair for duplicates.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False


def find_duplicates_fast(lst):
    """
    TODO: Write an O(n) version using a set.

    Hint: Sets have O(1) lookup time.
    Check if item is in set, if not add it.
    """
    # TODO: Implement faster version
    pass


# =============================================================================
# TODO: Exercise 4 - Two Sum Problem
# =============================================================================

def two_sum_slow(lst, target):
    """
    O(n²) - Find two numbers that add to target.
    Returns indices of the two numbers, or None.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (i, j)
    return None


def two_sum_fast(lst, target):
    """
    TODO: Write an O(n) version using a dictionary.

    For each number, check if (target - number) has been seen.
    Store {number: index} as you go.
    """
    # TODO: Implement faster version
    pass


# =============================================================================
# Demonstration
# =============================================================================

def demo_efficiency():
    """Demonstrate how complexity affects real-world performance."""
    print("\nDemonstrating Algorithm Efficiency")
    print("=" * 50)

    # Small list
    small = list(range(1000))
    _, t1 = time_function(linear_time_example, small)
    _, t2 = time_function(quadratic_time_example, small)
    print(f"\n1,000 items:")
    print(f"  O(n):  {t1:.6f} seconds")
    print(f"  O(n²): {t2:.6f} seconds")
    print(f"  Ratio: {t2/t1:.1f}x slower")

    # Medium list
    medium = list(range(5000))
    _, t1 = time_function(linear_time_example, medium)
    _, t2 = time_function(quadratic_time_example, medium)
    print(f"\n5,000 items:")
    print(f"  O(n):  {t1:.6f} seconds")
    print(f"  O(n²): {t2:.6f} seconds")
    print(f"  Ratio: {t2/t1:.1f}x slower")

    print("\nAs data grows, O(n²) becomes impractical!")


if __name__ == "__main__":
    print("=" * 50)
    print("Week 8: Algorithm Efficiency")
    print("=" * 50)

    # Run demo
    demo_efficiency()

    # Uncomment to compare:
    # compare_linear_vs_quadratic()
