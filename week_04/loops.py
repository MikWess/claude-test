"""
Week 4: Loops and Iteration Practice
=====================================
Big Idea: AAP (Algorithms and Programming)

Practice for and while loops with various problems.
"""

# =============================================================================
# Example: For Loop
# =============================================================================

def for_loop_example():
    """Demonstrate basic for loop usage."""
    print("Counting to 5:")
    for i in range(1, 6):
        print(f"  {i}")

    print("\nSquares from 1 to 5:")
    for num in range(1, 6):
        print(f"  {num}² = {num ** 2}")


# =============================================================================
# TODO: Exercise 1 - Sum of Numbers
# =============================================================================

def sum_to_n(n):
    """
    Calculate the sum of all numbers from 1 to n.

    Args:
        n: The upper limit (inclusive)

    Returns:
        Sum of 1 + 2 + 3 + ... + n

    Examples:
        sum_to_n(5) → 15  (1+2+3+4+5)
        sum_to_n(10) → 55
    """
    # TODO: Use a for loop to calculate the sum
    pass


# =============================================================================
# TODO: Exercise 2 - Factorial
# =============================================================================

def factorial(n):
    """
    Calculate n! (n factorial).
    n! = n × (n-1) × (n-2) × ... × 2 × 1

    Args:
        n: A non-negative integer

    Returns:
        n factorial

    Examples:
        factorial(5) → 120  (5×4×3×2×1)
        factorial(0) → 1    (by definition)
    """
    # TODO: Implement using a loop
    pass


# =============================================================================
# TODO: Exercise 3 - FizzBuzz
# =============================================================================

def fizzbuzz(n):
    """
    Print numbers from 1 to n with the following rules:
    - If divisible by 3, print "Fizz"
    - If divisible by 5, print "Buzz"
    - If divisible by both 3 and 5, print "FizzBuzz"
    - Otherwise, print the number

    Args:
        n: The upper limit

    Example output for n=15:
        1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
    """
    # TODO: Implement FizzBuzz
    pass


# =============================================================================
# TODO: Exercise 4 - Guess the Number (While Loop)
# =============================================================================

def guess_the_number():
    """
    Simple number guessing game using a while loop.

    1. Pick a secret number between 1 and 100
    2. Let the user guess
    3. Tell them if guess is too high, too low, or correct
    4. Count the number of guesses
    5. End when they guess correctly

    Hint: Use random.randint(1, 100) for the secret number
    """
    import random
    # TODO: Implement the game
    pass


# =============================================================================
# TODO: Exercise 5 - Pattern Printing (Nested Loops)
# =============================================================================

def print_triangle(n):
    """
    Print a right triangle pattern of asterisks.

    Args:
        n: Number of rows

    Example for n=5:
        *
        **
        ***
        ****
        *****
    """
    # TODO: Use nested loops to print the pattern
    pass


def print_pyramid(n):
    """
    Print a centered pyramid pattern.

    Args:
        n: Number of rows

    Example for n=5:
        *
       ***
      *****
     *******
    *********
    """
    # TODO: This is a challenge! Think about spaces and stars.
    pass


# =============================================================================
# TODO: Exercise 6 - Find Prime Numbers
# =============================================================================

def find_primes(n):
    """
    Find all prime numbers from 2 to n.

    A prime number is only divisible by 1 and itself.

    Args:
        n: Upper limit

    Returns:
        List of prime numbers

    Example:
        find_primes(20) → [2, 3, 5, 7, 11, 13, 17, 19]
    """
    # TODO: Implement using nested loops
    # Hint: For each number, check if it's divisible by any smaller number
    pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    """Test the exercises."""
    print("Running tests...\n")

    # Test sum_to_n
    if sum_to_n:
        assert sum_to_n(5) == 15
        assert sum_to_n(10) == 55
        assert sum_to_n(1) == 1
        print("✓ sum_to_n tests passed")

    # Test factorial
    if factorial:
        assert factorial(5) == 120
        assert factorial(0) == 1
        assert factorial(1) == 1
        print("✓ factorial tests passed")

    # Test find_primes
    if find_primes:
        primes = find_primes(20)
        assert primes == [2, 3, 5, 7, 11, 13, 17, 19]
        print("✓ find_primes tests passed")

    print("\nAll tests passed!")


if __name__ == "__main__":
    print("=" * 50)
    print("Week 4: Loops and Iteration")
    print("=" * 50)

    # Show examples
    for_loop_example()

    # Uncomment to test:
    # print_triangle(5)
    # fizzbuzz(15)
    # guess_the_number()
    # run_tests()
