"""
Control Flow: Functions
=======================
Learn about defining and using functions.
"""

# =============================================================================
# LESSON: Basic function definition
# =============================================================================

def greet(name):
    """Greet someone by name."""
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
greet("Bob")


# =============================================================================
# LESSON: Functions with return values
# =============================================================================

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def square(n):
    """Return n squared."""
    return n ** 2

result = add(5, 3)
print(f"5 + 3 = {result}")
print(f"4 squared = {square(4)}")


# =============================================================================
# EXERCISE 1: Basic functions
# =============================================================================
# TODO: Define these functions

# Function: multiply(a, b)
# Returns: the product of a and b
def multiply(a, b):
    pass  # TODO: Replace pass with your code


# Function: is_even(n)
# Returns: True if n is even, False otherwise
def is_even(n):
    pass  # TODO


# Function: get_initials(first_name, last_name)
# Returns: the first letter of each name, uppercased
# Example: get_initials("john", "doe") -> "JD"
def get_initials(first_name, last_name):
    pass  # TODO


# Uncomment to test:
# print(f"\nmultiply(4, 5) = {multiply(4, 5)}")
# print(f"is_even(7) = {is_even(7)}")
# print(f"is_even(8) = {is_even(8)}")
# print(f"get_initials('john', 'doe') = {get_initials('john', 'doe')}")


# =============================================================================
# LESSON: Default parameters
# =============================================================================

def greet_with_title(name, title="Mr."):
    """Greet with an optional title."""
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")           # Uses default "Mr."
greet_with_title("Johnson", "Dr.")  # Overrides default


# =============================================================================
# EXERCISE 2: Default parameters
# =============================================================================
# TODO: Create a function with default parameters

# Function: calculate_tip(bill, tip_percent=0.18)
# Returns: the tip amount
# Example: calculate_tip(100) -> 18.0
# Example: calculate_tip(100, 0.20) -> 20.0
def calculate_tip(bill, tip_percent=0.18):
    pass  # TODO


# Uncomment to test:
# print(f"\ncalculate_tip(100) = ${calculate_tip(100):.2f}")
# print(f"calculate_tip(100, 0.20) = ${calculate_tip(100, 0.20):.2f}")


# =============================================================================
# LESSON: Multiple return values
# =============================================================================

def divide_with_remainder(a, b):
    """Return both quotient and remainder."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"\n17 ÷ 5 = {q} remainder {r}")


# =============================================================================
# EXERCISE 3: Multiple return values
# =============================================================================
# TODO: Create a function that returns multiple values

# Function: get_stats(numbers)
# Returns: minimum, maximum, and average of the list
# Example: get_stats([1, 2, 3, 4, 5]) -> (1, 5, 3.0)
def get_stats(numbers):
    pass  # TODO: Return min, max, and average


# Uncomment to test:
# test_nums = [10, 20, 30, 40, 50]
# minimum, maximum, average = get_stats(test_nums)
# print(f"\nStats for {test_nums}:")
# print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")


# =============================================================================
# LESSON: Docstrings and the main pattern
# =============================================================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area (length * width)
    """
    return length * width


# The main pattern - only runs when file is executed directly
def main():
    """Main function to demonstrate the module."""
    area = calculate_area(5, 3)
    print(f"\nArea of 5x3 rectangle: {area}")


# =============================================================================
# EXERCISE 4: Complete program
# =============================================================================
# TODO: Write a complete program with multiple functions

# Create these functions:

# 1. celsius_to_fahrenheit(celsius)
#    Formula: F = C * 9/5 + 32
def celsius_to_fahrenheit(celsius):
    pass  # TODO


# 2. fahrenheit_to_celsius(fahrenheit)
#    Formula: C = (F - 32) * 5/9
def fahrenheit_to_celsius(fahrenheit):
    pass  # TODO


# 3. print_conversion_table()
#    Print a table showing Celsius 0, 10, 20, 30, 40 and their Fahrenheit equivalents
def print_conversion_table():
    pass  # TODO


# =============================================================================
# EXERCISE 5: Recursive function (bonus!)
# =============================================================================
# TODO: Write a recursive function

# Function: factorial(n)
# Returns: n! (n factorial)
# Example: factorial(5) -> 120 (5 * 4 * 3 * 2 * 1)
# Hint: factorial(n) = n * factorial(n-1), and factorial(0) = 1
def factorial(n):
    pass  # TODO


# Function: fibonacci(n)
# Returns: the nth Fibonacci number
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Example: fibonacci(6) -> 8
def fibonacci(n):
    pass  # TODO


# Uncomment to test:
# print(f"\nfactorial(5) = {factorial(5)}")
# print(f"First 10 Fibonacci numbers: ", end="")
# for i in range(10):
#     print(fibonacci(i), end=" ")
# print()


if __name__ == "__main__":
    main()
    print("\n" + "="*50)
    print("Complete the exercises above!")
    print("="*50)
