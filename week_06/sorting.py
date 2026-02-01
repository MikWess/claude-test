"""
Week 6: Sorting Algorithms
==========================
Big Idea: AAP (Algorithms and Programming)

Implement and understand basic sorting algorithms.
"""

# =============================================================================
# Bubble Sort - Example
# =============================================================================

def bubble_sort(lst):
    """
    Sort list using bubble sort (in-place).
    Repeatedly swaps adjacent elements if they're in wrong order.
    """
    lst = lst.copy()  # Don't modify original
    n = len(lst)

    for i in range(n):
        # Flag to optimize - if no swaps, list is sorted
        swapped = False

        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

    return lst


# =============================================================================
# TODO: Exercise 1 - Selection Sort
# =============================================================================

def selection_sort(lst):
    """
    Sort list using selection sort.

    Algorithm:
    1. Find the minimum element in unsorted portion
    2. Swap it with the first unsorted element
    3. Repeat for remaining unsorted portion

    Args:
        lst: List to sort

    Returns:
        New sorted list

    Example:
        selection_sort([64, 25, 12, 22, 11]) → [11, 12, 22, 25, 64]
    """
    lst = lst.copy()
    # TODO: Implement selection sort
    pass


# =============================================================================
# TODO: Exercise 2 - Insertion Sort
# =============================================================================

def insertion_sort(lst):
    """
    Sort list using insertion sort.

    Algorithm:
    1. Start with second element
    2. Insert it into correct position among previous elements
    3. Repeat for all remaining elements

    Like sorting cards in your hand.

    Args:
        lst: List to sort

    Returns:
        New sorted list
    """
    lst = lst.copy()
    # TODO: Implement insertion sort
    pass


# =============================================================================
# TODO: Exercise 3 - Sort Visualization
# =============================================================================

def visualize_bubble_sort(lst):
    """
    Show each step of bubble sort.

    Example output:
        [5, 3, 8, 1] - Starting
        [3, 5, 8, 1] - Swapped 5 and 3
        [3, 5, 1, 8] - Swapped 8 and 1
        [3, 1, 5, 8] - Swapped 5 and 1
        [1, 3, 5, 8] - Swapped 3 and 1
        [1, 3, 5, 8] - Sorted!
    """
    # TODO: Implement with print statements showing each swap
    pass


# =============================================================================
# TODO: Exercise 4 - Count Comparisons
# =============================================================================

def bubble_sort_count(lst):
    """
    Bubble sort that counts comparisons and swaps.

    Returns:
        tuple: (sorted_list, comparison_count, swap_count)
    """
    # TODO: Implement with counting
    pass


def selection_sort_count(lst):
    """
    Selection sort that counts comparisons and swaps.

    Returns:
        tuple: (sorted_list, comparison_count, swap_count)
    """
    # TODO: Implement with counting
    pass


# =============================================================================
# TODO: Exercise 5 - Compare Algorithms
# =============================================================================

def compare_sorts():
    """
    Compare sorting algorithms on different types of data.

    Test with:
    1. Random list
    2. Already sorted list
    3. Reverse sorted list
    4. List with many duplicates
    """
    import random

    test_cases = [
        ("Random", [random.randint(1, 100) for _ in range(20)]),
        ("Sorted", list(range(1, 21))),
        ("Reverse", list(range(20, 0, -1))),
        ("Duplicates", [5, 3, 5, 1, 3, 5, 1, 3, 5, 1]),
    ]

    print("Comparison of Sorting Algorithms")
    print("=" * 60)

    for name, data in test_cases:
        print(f"\n{name} data: {data[:5]}... (length {len(data)})")
        # TODO: Run both sorts with counting and compare
        pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    """Test sorting implementations."""
    print("Running tests...\n")

    test_cases = [
        [64, 25, 12, 22, 11],
        [5, 1, 4, 2, 8],
        [1],
        [],
        [3, 3, 3, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    for test in test_cases:
        expected = sorted(test)

        # Test bubble sort
        assert bubble_sort(test) == expected, f"Bubble sort failed on {test}"

        # Test selection sort
        if selection_sort(test) is not None:
            assert selection_sort(test) == expected, f"Selection sort failed on {test}"

        # Test insertion sort
        if insertion_sort(test) is not None:
            assert insertion_sort(test) == expected, f"Insertion sort failed on {test}"

    print("✓ All sorting tests passed!")


if __name__ == "__main__":
    print("=" * 50)
    print("Week 6: Sorting Algorithms")
    print("=" * 50)

    # Demo bubble sort
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal: {data}")
    print(f"Bubble sorted: {bubble_sort(data)}")

    # Uncomment to run:
    # run_tests()
    # compare_sorts()
    # visualize_bubble_sort([5, 3, 8, 1])
