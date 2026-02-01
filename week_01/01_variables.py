"""
Python Basics: Variables and Data Types
========================================
Learn about variables, data types, and basic operations.
"""

# =============================================================================
# LESSON: Variables store data. Python figures out the type automatically.
# =============================================================================

# Example: Creating variables
name = "Alice"          # str (string)
age = 25                # int (integer)
height = 5.7            # float (decimal)
is_student = True       # bool (boolean)

# Printing variables
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")


# =============================================================================
# EXERCISE 1: Create variables for yourself
# =============================================================================
# TODO: Create variables for your name, age, favorite number, and whether you like pizza

your_name = None        # Replace None with your name as a string
your_age = None         # Replace None with your age as an integer
fav_number = None       # Replace None with your favorite number
likes_pizza = None      # Replace None with True or False

# Uncomment when ready:
# print(f"Hi, I'm {your_name}! I'm {your_age} years old.")
# print(f"My favorite number is {fav_number}. Likes pizza: {likes_pizza}")


# =============================================================================
# LESSON: Type conversion - changing one type to another
# =============================================================================

# Converting types
str_number = "42"
actual_number = int(str_number)     # str -> int
back_to_string = str(actual_number) # int -> str
as_float = float(str_number)        # str -> float

print(f"Original: '{str_number}' (type: {type(str_number).__name__})")
print(f"As int: {actual_number} (type: {type(actual_number).__name__})")
print(f"As float: {as_float} (type: {type(as_float).__name__})")


# =============================================================================
# EXERCISE 2: Type conversion practice
# =============================================================================
# TODO: Convert these variables to the requested types

price_string = "19.99"
quantity_string = "5"

# Convert price_string to a float
price = None  # TODO

# Convert quantity_string to an integer
quantity = None  # TODO

# Calculate total (price * quantity)
total = None  # TODO

# Uncomment when ready:
# print(f"Price: ${price}, Quantity: {quantity}, Total: ${total}")


# =============================================================================
# LESSON: String operations
# =============================================================================

message = "Hello, World!"

print(f"Original: {message}")
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
print(f"Length: {len(message)}")
print(f"First character: {message[0]}")
print(f"Last character: {message[-1]}")
print(f"First 5 characters: {message[:5]}")


# =============================================================================
# EXERCISE 3: String manipulation
# =============================================================================
# TODO: Complete the string exercises

sentence = "python is awesome"

# Make the first letter uppercase (capitalize)
capitalized = None  # TODO: use .capitalize()

# Count how many times 'o' appears
o_count = None  # TODO: use .count()

# Replace 'awesome' with 'fun'
new_sentence = None  # TODO: use .replace()

# Uncomment when ready:
# print(f"Capitalized: {capitalized}")
# print(f"Letter 'o' appears {o_count} times")
# print(f"New sentence: {new_sentence}")


# =============================================================================
# EXERCISE 4: User input (run this file to test!)
# =============================================================================
# TODO: Uncomment and complete the input exercise

# Ask user for their name and favorite color
# user_name = input("What is your name? ")
# user_color = input("What is your favorite color? ")
# print(f"Nice to meet you, {user_name}! {user_color} is a great color!")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Run this file to test your solutions!")
    print("="*50)
