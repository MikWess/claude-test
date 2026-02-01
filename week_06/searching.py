"""
Week 6: Searching Algorithms
============================
Big Idea: AAP (Algorithms and Programming)

Implement and understand linear search and binary search.
"""

# =============================================================================
# Linear Search - Example
# =============================================================================

def linear_search(lst, target):
    """
    Search for target in list using linear search.
    Returns index if found, -1 if not found.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# =============================================================================
# TODO: Exercise 1 - Linear Search with Count
# =============================================================================

def linear_search_count(lst, target):
    """
    Search for target and count how many comparisons were made.

    Args:
        lst: List to search
        target: Value to find

    Returns:
        tuple: (index or -1, comparison_count)

    Example:
        linear_search_count([5, 3, 8, 1, 9], 8) → (2, 3)
        # Found at index 2, took 3 comparisons
    """
    # TODO: Implement with comparison counting
    pass


# =============================================================================
# TODO: Exercise 2 - Binary Search
# =============================================================================

def binary_search(lst, target):
    """
    Search for target in SORTED list using binary search.

    The list MUST be sorted for this to work correctly!

    Args:
        lst: Sorted list to search
        target: Value to find

    Returns:
        Index if found, -1 if not found

    Example:
        binary_search([1, 3, 5, 7, 9, 11], 7) → 3
    """
    # TODO: Implement binary search
    # Steps:
    # 1. Set low = 0, high = len(lst) - 1
    # 2. While low <= high:
    #    a. Calculate mid = (low + high) // 2
    #    b. If lst[mid] == target, return mid
    #    c. If lst[mid] < target, search right half (low = mid + 1)
    #    d. If lst[mid] > target, search left half (high = mid - 1)
    # 3. Return -1 if not found
    pass


# =============================================================================
# TODO: Exercise 3 - Binary Search with Count
# =============================================================================

def binary_search_count(lst, target):
    """
    Binary search that counts comparisons.

    Args:
        lst: Sorted list
        target: Value to find

    Returns:
        tuple: (index or -1, comparison_count)

    Example:
        binary_search_count([1,2,3,4,5,6,7,8], 6) → (5, 3)
    """
    # TODO: Implement with comparison counting
    pass


# =============================================================================
# TODO: Exercise 4 - Compare Algorithms
# =============================================================================

def compare_searches(size=1000):
    """
    Compare linear and binary search on a list of given size.

    1. Create a sorted list of numbers 1 to size
    2. Search for: first element, middle element, last element, not found
    3. Print comparison counts for both algorithms
    """
    import random

    # Create sorted list
    lst = list(range(1, size + 1))

    targets = [1, size // 2, size, size + 1]  # first, middle, last, not found

    print(f"Comparing searches on list of {size} elements:")
    print("-" * 50)
    print(f"{'Target':<12} {'Linear':<12} {'Binary':<12}")
    print("-" * 50)

    for target in targets:
        # TODO: Use your counting functions to compare
        # linear_count = linear_search_count(lst, target)[1]
        # binary_count = binary_search_count(lst, target)[1]
        # print(f"{target:<12} {linear_count:<12} {binary_count:<12}")
        pass


# =============================================================================
# TODO: Exercise 5 - Find First Occurrence
# =============================================================================

def find_first(lst, target):
    """
    Find the FIRST occurrence of target in a sorted list with duplicates.

    Args:
        lst: Sorted list (may contain duplicates)
        target: Value to find

    Returns:
        Index of first occurrence, or -1 if not found

    Example:
        find_first([1, 2, 2, 2, 3, 4], 2) → 1  (not 2 or 3)
    """
    # TODO: Modify binary search to find first occurrence
    # Hint: When you find target, check if it's the first one
    pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    """Test the search implementations."""
    print("Running tests...\n")

    # Test data
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    unsorted_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]

    # Test linear search
    assert linear_search(unsorted_list, 8) == 2
    assert linear_search(unsorted_list, 10) == -1
    print("✓ linear_search works")

    # Test binary search
    if binary_search:
        assert binary_search(sorted_list, 7) == 3
        assert binary_search(sorted_list, 1) == 0
        assert binary_search(sorted_list, 19) == 9
        assert binary_search(sorted_list, 10) == -1
        print("✓ binary_search works")

    # Test find_first
    if find_first:
        duplicates = [1, 2, 2, 2, 3, 3, 4, 5]
        assert find_first(duplicates, 2) == 1
        assert find_first(duplicates, 3) == 4
        print("✓ find_first works")

    print("\nAll tests passed!")


if __name__ == "__main__":
    print("=" * 50)
    print("Week 6: Searching Algorithms")
    print("=" * 50)

    # Demo
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"\nList: {numbers}")
    print(f"Linear search for 23: index {linear_search(numbers, 23)}")

    # Uncomment to run:
    # run_tests()
    # compare_searches(1000)
