"""
Week 9: Functions and Procedural Abstraction
=============================================
Big Ideas: AAP, CRD

Practice writing and using functions.
"""

# =============================================================================
# Example: Basic Functions
# =============================================================================

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# =============================================================================
# TODO: Exercise 1 - Temperature Conversion Functions
# =============================================================================

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius: Temperature in Celsius

    Returns:
        Temperature in Fahrenheit
    """
    # TODO: Implement
    pass


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit: Temperature in Fahrenheit

    Returns:
        Temperature in Celsius
    """
    # TODO: Implement
    pass


# =============================================================================
# TODO: Exercise 2 - String Functions
# =============================================================================

def is_palindrome(text):
    """
    Check if a string is a palindrome (reads same forwards and backwards).
    Ignore case and spaces.

    Args:
        text: String to check

    Returns:
        True if palindrome, False otherwise

    Examples:
        is_palindrome("racecar") → True
        is_palindrome("A man a plan a canal Panama") → True
        is_palindrome("hello") → False
    """
    # TODO: Implement
    pass


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    Case insensitive.

    Args:
        text: String to analyze

    Returns:
        Number of vowels

    Examples:
        count_vowels("Hello World") → 3
    """
    # TODO: Implement
    pass


# =============================================================================
# TODO: Exercise 3 - List Processing Functions
# =============================================================================

def find_min_max(numbers):
    """
    Find both minimum and maximum values in a list.

    Args:
        numbers: List of numbers

    Returns:
        Tuple of (minimum, maximum)

    Example:
        find_min_max([3, 1, 4, 1, 5, 9]) → (1, 9)
    """
    # TODO: Implement WITHOUT using built-in min() and max()
    pass


def remove_duplicates(lst):
    """
    Remove duplicate values from a list while preserving order.

    Args:
        lst: List with possible duplicates

    Returns:
        New list without duplicates

    Example:
        remove_duplicates([1, 2, 2, 3, 1, 4]) → [1, 2, 3, 4]
    """
    # TODO: Implement
    pass


# =============================================================================
# TODO: Exercise 4 - Functions with Multiple Returns
# =============================================================================

def analyze_numbers(numbers):
    """
    Analyze a list of numbers and return statistics.

    Args:
        numbers: List of numbers

    Returns:
        Dictionary with keys: 'count', 'sum', 'average', 'min', 'max'

    Example:
        analyze_numbers([1, 2, 3, 4, 5])
        → {'count': 5, 'sum': 15, 'average': 3.0, 'min': 1, 'max': 5}
    """
    # TODO: Implement
    pass


# =============================================================================
# TODO: Exercise 5 - Higher-Order Functions
# =============================================================================

def apply_to_all(lst, func):
    """
    Apply a function to every element in a list.

    Args:
        lst: List of values
        func: Function to apply

    Returns:
        New list with function applied

    Example:
        apply_to_all([1, 2, 3], lambda x: x * 2) → [2, 4, 6]
    """
    # TODO: Implement
    pass


def filter_list(lst, condition):
    """
    Keep only elements that satisfy a condition.

    Args:
        lst: List of values
        condition: Function that returns True/False

    Returns:
        New list with only elements where condition is True

    Example:
        filter_list([1, 2, 3, 4, 5], lambda x: x > 3) → [4, 5]
    """
    # TODO: Implement
    pass


# =============================================================================
# TODO: Exercise 6 - Putting It Together
# =============================================================================

def grade_calculator(scores, weights=None):
    """
    Calculate weighted grade from a list of scores.

    Args:
        scores: List of scores (0-100)
        weights: Optional list of weights (should sum to 1.0)
                 If None, use equal weights

    Returns:
        Dictionary with 'weighted_average' and 'letter_grade'

    Letter grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
    """
    # TODO: Implement
    pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    """Test function implementations."""
    print("Running tests...\n")

    # Temperature conversion
    if celsius_to_fahrenheit:
        assert abs(celsius_to_fahrenheit(0) - 32) < 0.01
        assert abs(celsius_to_fahrenheit(100) - 212) < 0.01
        print("✓ celsius_to_fahrenheit works")

    if fahrenheit_to_celsius:
        assert abs(fahrenheit_to_celsius(32) - 0) < 0.01
        assert abs(fahrenheit_to_celsius(212) - 100) < 0.01
        print("✓ fahrenheit_to_celsius works")

    # String functions
    if is_palindrome:
        assert is_palindrome("racecar") == True
        assert is_palindrome("hello") == False
        print("✓ is_palindrome works")

    if count_vowels:
        assert count_vowels("Hello World") == 3
        assert count_vowels("xyz") == 0
        print("✓ count_vowels works")

    # List functions
    if find_min_max:
        assert find_min_max([3, 1, 4, 1, 5, 9]) == (1, 9)
        print("✓ find_min_max works")

    if remove_duplicates:
        assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
        print("✓ remove_duplicates works")

    print("\nAll tests passed!")


if __name__ == "__main__":
    print("=" * 50)
    print("Week 9: Functions and Abstraction")
    print("=" * 50)

    # Demo
    print(f"\ngreet('World') = {greet('World')}")
    print(f"calculate_average([1,2,3,4,5]) = {calculate_average([1,2,3,4,5])}")

    # Uncomment to run tests:
    # run_tests()
