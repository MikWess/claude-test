"""
Error Handling: Exceptions
==========================
Learn about try/except and handling errors gracefully.
"""

# =============================================================================
# LESSON: Why error handling matters
# =============================================================================

# Without error handling, this crashes:
# number = int("hello")  # ValueError!
# result = 10 / 0        # ZeroDivisionError!


# =============================================================================
# LESSON: Basic try/except
# =============================================================================

# Catching a specific error
try:
    number = int("hello")
except ValueError:
    print("That's not a valid number!")

# Catching multiple error types
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")

# Getting error details
try:
    number = int("abc")
except ValueError as e:
    print(f"Error occurred: {e}")


# =============================================================================
# EXERCISE 1: Safe input
# =============================================================================
# TODO: Create a function that safely gets a number from user

def get_integer(prompt):
    """
    Keep asking until user enters a valid integer.
    Returns the integer.
    """
    # TODO:
    # Use a while True loop
    # Try to convert input to int
    # If ValueError, print error and continue
    # If successful, return the number
    pass

# Uncomment to test (interactive):
# age = get_integer("Enter your age: ")
# print(f"You entered: {age}")


# =============================================================================
# LESSON: try/except/else/finally
# =============================================================================

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    else:
        # Runs if NO exception occurred
        print(f"Success! {a} / {b} = {result}")
        return result
    finally:
        # ALWAYS runs, even if there was an error
        print("Division operation complete.")

print("\n")
divide(10, 2)
print()
divide(10, 0)


# =============================================================================
# EXERCISE 2: Safe file reader
# =============================================================================
# TODO: Create a safe file reading function

def read_file_safe(filepath):
    """
    Safely read a file and return its contents.
    Returns None if file doesn't exist or can't be read.
    Prints appropriate error messages.
    """
    # TODO:
    # Handle FileNotFoundError
    # Handle PermissionError
    # Handle any other exception
    # Use finally to print "File operation complete"
    pass

# Uncomment to test:
# content = read_file_safe("nonexistent.txt")
# print(f"Content: {content}")


# =============================================================================
# LESSON: Common exception types
# =============================================================================

print("\nCommon exceptions:")

# ValueError - wrong type of value
try:
    int("not a number")
except ValueError as e:
    print(f"ValueError: {e}")

# TypeError - wrong type for operation
try:
    "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# KeyError - dictionary key not found
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print(f"KeyError: {e}")

# IndexError - list index out of range
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"IndexError: {e}")


# =============================================================================
# EXERCISE 3: Safe dictionary access
# =============================================================================
# TODO: Create a function for safe nested dictionary access

def safe_get(dictionary, *keys, default=None):
    """
    Safely access nested dictionary keys.

    Example:
        data = {"user": {"name": "Alice", "age": 25}}
        safe_get(data, "user", "name")  # Returns "Alice"
        safe_get(data, "user", "email", default="N/A")  # Returns "N/A"
    """
    # TODO:
    # Loop through keys
    # Try to access each nested level
    # Return default if KeyError occurs
    pass

# Uncomment to test:
# data = {
#     "user": {
#         "profile": {
#             "name": "Alice",
#             "settings": {"theme": "dark"}
#         }
#     }
# }
# print(f"\nName: {safe_get(data, 'user', 'profile', 'name')}")
# print(f"Theme: {safe_get(data, 'user', 'profile', 'settings', 'theme')}")
# print(f"Email: {safe_get(data, 'user', 'profile', 'email', default='Not set')}")
# print(f"Missing: {safe_get(data, 'foo', 'bar', default='N/A')}")


# =============================================================================
# EXERCISE 4: Calculator with error handling
# =============================================================================
# TODO: Build a calculator that handles all edge cases

def calculator(expression):
    """
    Evaluate a simple math expression like "10 + 5" or "20 / 4".
    Supports: +, -, *, /

    Returns the result or an error message string.
    """
    # TODO:
    # 1. Split expression into parts (num1, operator, num2)
    # 2. Handle ValueError if numbers are invalid
    # 3. Handle ZeroDivisionError for division
    # 4. Handle unknown operators
    pass

# Uncomment to test:
# print("\nCalculator:")
# print(f"10 + 5 = {calculator('10 + 5')}")
# print(f"20 / 4 = {calculator('20 / 4')}")
# print(f"10 / 0 = {calculator('10 / 0')}")
# print(f"abc + 5 = {calculator('abc + 5')}")
# print(f"10 ^ 2 = {calculator('10 ^ 2')}")


# =============================================================================
# LESSON: Raising exceptions
# =============================================================================

def validate_age(age):
    """Validate that age is reasonable."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"\nValidation error: {e}")


# =============================================================================
# EXERCISE 5: Input validation
# =============================================================================
# TODO: Create validation functions that raise appropriate exceptions

def validate_email(email):
    """
    Validate an email address.
    Raise ValueError with descriptive message if invalid.

    Requirements:
    - Must contain exactly one @
    - Must have something before and after @
    - Part after @ must contain a dot
    """
    # TODO
    pass

def validate_password(password):
    """
    Validate a password.
    Raise ValueError with descriptive message if invalid.

    Requirements:
    - At least 8 characters
    - Contains at least one digit
    - Contains at least one uppercase letter
    """
    # TODO
    pass

# Uncomment to test:
# test_emails = ["test@example.com", "invalid", "no@dot", "@missing.com"]
# for email in test_emails:
#     try:
#         validate_email(email)
#         print(f"'{email}' - Valid")
#     except ValueError as e:
#         print(f"'{email}' - Invalid: {e}")

# print()
# test_passwords = ["SecurePass1", "short", "nouppercase1", "NoDigits"]
# for pwd in test_passwords:
#     try:
#         validate_password(pwd)
#         print(f"'{pwd}' - Valid")
#     except ValueError as e:
#         print(f"'{pwd}' - Invalid: {e}")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Complete the exercises above!")
    print("="*50)
