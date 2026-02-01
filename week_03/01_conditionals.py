"""
Control Flow: Conditionals
==========================
Learn about if/elif/else statements and comparison operators.
"""

# =============================================================================
# LESSON: Comparison operators
# =============================================================================

x = 10
y = 5

print("Comparison Operators:")
print(f"{x} == {y}: {x == y}")   # Equal to
print(f"{x} != {y}: {x != y}")   # Not equal to
print(f"{x} > {y}: {x > y}")     # Greater than
print(f"{x} < {y}: {x < y}")     # Less than
print(f"{x} >= {y}: {x >= y}")   # Greater than or equal
print(f"{x} <= {y}: {x <= y}")   # Less than or equal


# =============================================================================
# LESSON: if/elif/else statements
# =============================================================================

age = 18

if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're an adult")
else:
    print("You're a senior")


# =============================================================================
# EXERCISE 1: Grade calculator
# =============================================================================
# TODO: Write conditions to determine the letter grade

score = 85

# Grading scale:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

grade = None  # TODO: Use if/elif/else to set the grade

# Uncomment when ready:
# print(f"Score: {score} -> Grade: {grade}")


# =============================================================================
# LESSON: Logical operators (and, or, not)
# =============================================================================

age = 25
has_license = True
is_insured = True

# and - both must be True
can_drive = age >= 16 and has_license
print(f"\nCan drive (age >= 16 AND has license): {can_drive}")

# or - at least one must be True
has_coverage = has_license or is_insured
print(f"Has coverage (license OR insured): {has_coverage}")

# not - inverts the boolean
is_minor = not (age >= 18)
print(f"Is minor (NOT adult): {is_minor}")


# =============================================================================
# EXERCISE 2: Access control
# =============================================================================
# TODO: Determine if a user can access a feature

user_age = 21
is_member = True
has_permission = False

# A user can access the feature if:
# - They are at least 18 years old AND a member, OR
# - They have explicit permission

can_access = None  # TODO: Write the logical expression

# Uncomment when ready:
# print(f"\nUser can access feature: {can_access}")


# =============================================================================
# EXERCISE 3: Number classifier
# =============================================================================
# TODO: Classify a number based on multiple properties

number = -15

# Determine and print:
# 1. Is it positive, negative, or zero?
# 2. Is it even or odd? (hint: use % 2)
# 3. Is it a multiple of 5?

# TODO: Write the conditionals

# Example output:
# -15 is negative
# -15 is odd
# -15 is a multiple of 5


# =============================================================================
# EXERCISE 4: Simple login
# =============================================================================
# TODO: Check if login credentials are correct

correct_username = "admin"
correct_password = "secret123"

# Simulate user input (in real code, you'd use input())
entered_username = "admin"
entered_password = "secret123"

# Check if BOTH username and password are correct
# If yes: print "Login successful!"
# If username wrong: print "Invalid username"
# If password wrong: print "Invalid password"

# TODO: Write the conditionals


# =============================================================================
# LESSON: Ternary operator (one-line if/else)
# =============================================================================

age = 20
status = "adult" if age >= 18 else "minor"
print(f"\nAge {age}: {status}")

# Equivalent to:
# if age >= 18:
#     status = "adult"
# else:
#     status = "minor"


# =============================================================================
# EXERCISE 5: Ternary practice
# =============================================================================
# TODO: Rewrite these using ternary operators

temperature = 75

# If temperature > 80, hot = "Yes", else hot = "No"
is_hot = None  # TODO: Use ternary

# If temperature is between 60 and 80 (inclusive), weather = "Nice", else "Not ideal"
weather = None  # TODO: Use ternary

# Uncomment when ready:
# print(f"Temperature: {temperature}°F")
# print(f"Is it hot? {is_hot}")
# print(f"Weather: {weather}")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Complete the exercises above!")
    print("="*50)
