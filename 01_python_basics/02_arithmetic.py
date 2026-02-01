"""
Python Basics: Arithmetic Operations
=====================================
Learn about math operations and number formatting.
"""

# =============================================================================
# LESSON: Basic arithmetic operators
# =============================================================================

a = 15
b = 4

print("Basic Operations:")
print(f"{a} + {b} = {a + b}")   # Addition
print(f"{a} - {b} = {a - b}")   # Subtraction
print(f"{a} * {b} = {a * b}")   # Multiplication
print(f"{a} / {b} = {a / b}")   # Division (returns float)
print(f"{a} // {b} = {a // b}") # Floor division (integer result)
print(f"{a} % {b} = {a % b}")   # Modulo (remainder)
print(f"{a} ** {b} = {a ** b}") # Exponentiation (power)


# =============================================================================
# EXERCISE 1: Calculator
# =============================================================================
# TODO: Calculate the following

x = 100
y = 7

# What is x divided by y? (regular division)
division_result = None  # TODO

# What is the remainder when x is divided by y?
remainder = None  # TODO

# What is x to the power of 3?
cubed = None  # TODO

# Uncomment when ready:
# print(f"\n100 / 7 = {division_result}")
# print(f"100 % 7 = {remainder}")
# print(f"100 ** 3 = {cubed}")


# =============================================================================
# LESSON: Order of operations (PEMDAS)
# =============================================================================

# Python follows PEMDAS: Parentheses, Exponents, Mult/Div, Add/Sub
result1 = 2 + 3 * 4      # 14 (multiplication first)
result2 = (2 + 3) * 4    # 20 (parentheses first)
result3 = 2 ** 3 + 1     # 9 (exponent first)
result4 = 10 / 2 + 3     # 8.0 (division first)

print(f"\n2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")
print(f"2 ** 3 + 1 = {result3}")
print(f"10 / 2 + 3 = {result4}")


# =============================================================================
# EXERCISE 2: Order of operations
# =============================================================================
# TODO: Predict the result, then check by running

# What will these equal?
expr1 = 5 + 2 * 3 - 1      # Predict: ___
expr2 = (5 + 2) * (3 - 1)  # Predict: ___
expr3 = 2 ** 2 ** 2        # Predict: ___ (hint: right to left!)
expr4 = 20 // 3 * 2        # Predict: ___

# Uncomment to check your predictions:
# print(f"\n5 + 2 * 3 - 1 = {expr1}")
# print(f"(5 + 2) * (3 - 1) = {expr2}")
# print(f"2 ** 2 ** 2 = {expr3}")
# print(f"20 // 3 * 2 = {expr4}")


# =============================================================================
# LESSON: Floating point precision
# =============================================================================

# Computers can't perfectly represent all decimals
print(f"\n0.1 + 0.2 = {0.1 + 0.2}")  # Not exactly 0.3!

# Use round() to fix display issues
print(f"round(0.1 + 0.2, 2) = {round(0.1 + 0.2, 2)}")

# Formatting floats for display
pi = 3.14159265359
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Pi to 4 decimals: {pi:.4f}")


# =============================================================================
# EXERCISE 3: Money calculations
# =============================================================================
# TODO: Calculate prices with proper formatting

price = 19.99
quantity = 3
tax_rate = 0.08  # 8% tax

# Calculate subtotal (price * quantity)
subtotal = None  # TODO

# Calculate tax amount (subtotal * tax_rate)
tax = None  # TODO

# Calculate total (subtotal + tax)
total = None  # TODO

# Uncomment when ready (note the :.2f formatting for money):
# print(f"\nSubtotal: ${subtotal:.2f}")
# print(f"Tax (8%): ${tax:.2f}")
# print(f"Total: ${total:.2f}")


# =============================================================================
# EXERCISE 4: Temperature converter
# =============================================================================
# TODO: Convert temperatures

fahrenheit = 98.6

# Formula: Celsius = (Fahrenheit - 32) * 5/9
celsius = None  # TODO

# Uncomment when ready:
# print(f"\n{fahrenheit}°F = {celsius:.1f}°C")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Complete the TODOs and run to check your work!")
    print("="*50)
