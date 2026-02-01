"""
Week 2: Input and Output Practice
==================================
Big Idea: AAP (Algorithms and Programming)

Practice getting user input and displaying formatted output.
"""

# =============================================================================
# Example: Basic Input/Output
# =============================================================================

def greeting_example():
    """Example of basic input and output."""
    name = input("What is your name? ")
    print(f"Hello, {name}!")
    print("Welcome to Python programming.")


# =============================================================================
# TODO: Exercise 1 - Temperature Converter
# =============================================================================

def celsius_to_fahrenheit():
    """
    Ask the user for a temperature in Celsius and convert to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Example:
        Enter temperature in Celsius: 25
        25°C = 77.0°F
    """
    # TODO: Get temperature from user (remember to convert to float!)
    # TODO: Calculate Fahrenheit
    # TODO: Print the result
    pass


# =============================================================================
# TODO: Exercise 2 - Age Calculator
# =============================================================================

def calculate_age():
    """
    Ask for the user's birth year and calculate their age.
    Also tell them what year they'll turn 100.

    Example:
        What year were you born? 2000
        You are 25 years old.
        You will turn 100 in 2100!
    """
    # TODO: Implement this function
    pass


# =============================================================================
# TODO: Exercise 3 - Receipt Calculator
# =============================================================================

def calculate_receipt():
    """
    Create a simple receipt calculator.
    Ask for: item name, price, and quantity
    Calculate and display the total.

    Example:
        Item name: Apple
        Price per item: 1.50
        Quantity: 4

        === RECEIPT ===
        Apple x 4
        Total: $6.00
    """
    # TODO: Implement this function
    pass


# =============================================================================
# TODO: Exercise 4 - Mad Libs
# =============================================================================

def mad_libs():
    """
    Create a simple mad libs game.
    Ask for: a noun, a verb, an adjective, and an adverb
    Then print a silly sentence using all four words.

    Example:
        Enter a noun: cat
        Enter a verb: dances
        Enter an adjective: purple
        Enter an adverb: quickly

        The purple cat quickly dances around the room!
    """
    # TODO: Implement this function
    pass


# =============================================================================
# Run exercises
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Week 2: Input/Output Exercises")
    print("=" * 50)

    # Uncomment each function to test:
    # greeting_example()
    # celsius_to_fahrenheit()
    # calculate_age()
    # calculate_receipt()
    # mad_libs()

    print("\nUncomment functions in main to test them!")
