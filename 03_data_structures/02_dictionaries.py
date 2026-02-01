"""
Data Structures: Dictionaries
=============================
Learn about Python dictionaries - key-value pairs.
"""

# =============================================================================
# LESSON: Creating and accessing dictionaries
# =============================================================================

# Dictionary stores key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

print("Student:", student)
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# Using .get() - safer, returns None if key doesn't exist
print(f"Email: {student.get('email')}")
print(f"Email (with default): {student.get('email', 'N/A')}")


# =============================================================================
# EXERCISE 1: Dictionary basics
# =============================================================================
# TODO: Create and access a dictionary

# Create a dictionary for a book with:
# - title: "The Great Gatsby"
# - author: "F. Scott Fitzgerald"
# - year: 1925
# - pages: 180

book = None  # TODO: Create the dictionary

# Access the author
author = None  # TODO

# Use .get() to access "publisher" with default "Unknown"
publisher = None  # TODO

# Uncomment to test:
# print(f"\nBook: {book}")
# print(f"Author: {author}")
# print(f"Publisher: {publisher}")


# =============================================================================
# LESSON: Modifying dictionaries
# =============================================================================

person = {"name": "Bob", "age": 25}

# Adding/updating
person["email"] = "bob@email.com"  # Add new key
person["age"] = 26                  # Update existing

# Removing
del person["email"]                 # Remove key
# Or: person.pop("email")

# Update multiple at once
person.update({"city": "NYC", "job": "Developer"})

print(f"\nPerson: {person}")


# =============================================================================
# EXERCISE 2: Modifying dictionaries
# =============================================================================
# TODO: Modify this dictionary

profile = {
    "username": "coder123",
    "email": "old@email.com",
    "level": 1
}

# Update email to "new@email.com"
# TODO

# Add a "points" key with value 100
# TODO

# Increase level by 1
# TODO

# Add multiple: {"premium": True, "theme": "dark"}
# TODO

# Remove the "email" key
# TODO

# Uncomment to test:
# print(f"\nUpdated profile: {profile}")
# Expected keys: username, level, points, premium, theme


# =============================================================================
# LESSON: Dictionary methods
# =============================================================================

inventory = {"apples": 50, "bananas": 30, "oranges": 25}

print(f"\nKeys: {list(inventory.keys())}")
print(f"Values: {list(inventory.values())}")
print(f"Items: {list(inventory.items())}")

# Check if key exists
print(f"'apples' exists: {'apples' in inventory}")
print(f"'grapes' exists: {'grapes' in inventory}")


# =============================================================================
# EXERCISE 3: Dictionary iteration
# =============================================================================
# TODO: Iterate through this dictionary

prices = {
    "coffee": 4.50,
    "tea": 3.00,
    "juice": 5.00,
    "water": 1.50,
    "soda": 2.50
}

# Print all items in format "coffee: $4.50"
print("\nMenu:")
# TODO: Use a for loop with .items()


# Find the most expensive item
most_expensive = None  # TODO
highest_price = None   # TODO

# Find all items under $3
cheap_items = []  # TODO: Use a loop or comprehension

# Calculate total value of all items
total_value = None  # TODO: Use sum() with .values()

# Uncomment to test:
# print(f"\nMost expensive: {most_expensive} (${highest_price})")
# print(f"Items under $3: {cheap_items}")
# print(f"Total value: ${total_value}")


# =============================================================================
# LESSON: Nested dictionaries
# =============================================================================

school = {
    "class_a": {
        "teacher": "Ms. Smith",
        "students": 25,
        "room": 101
    },
    "class_b": {
        "teacher": "Mr. Jones",
        "students": 28,
        "room": 102
    }
}

print(f"\nClass A teacher: {school['class_a']['teacher']}")
print(f"Class B students: {school['class_b']['students']}")


# =============================================================================
# EXERCISE 4: Nested dictionaries
# =============================================================================
# TODO: Work with this nested dictionary

users = {
    "user1": {
        "name": "Alice",
        "scores": [85, 90, 88],
        "active": True
    },
    "user2": {
        "name": "Bob",
        "scores": [75, 80, 70],
        "active": True
    },
    "user3": {
        "name": "Charlie",
        "scores": [95, 92, 98],
        "active": False
    }
}

# Get Alice's average score
alice_avg = None  # TODO

# Get all active user names
active_users = []  # TODO

# Find the user with the highest average score
top_user = None  # TODO

# Uncomment to test:
# print(f"\nAlice's average: {alice_avg:.1f}")
# print(f"Active users: {active_users}")
# print(f"Top performer: {top_user}")


# =============================================================================
# LESSON: Dictionary comprehensions
# =============================================================================

# Create dict from list
numbers = [1, 2, 3, 4, 5]
squares = {n: n**2 for n in numbers}
print(f"\nSquares dict: {squares}")

# Filter a dictionary
prices = {"a": 10, "b": 25, "c": 5, "d": 30}
expensive = {k: v for k, v in prices.items() if v > 15}
print(f"Expensive items: {expensive}")


# =============================================================================
# EXERCISE 5: Dictionary comprehensions
# =============================================================================
# TODO: Create dictionaries using comprehensions

# 1. Create a dict mapping numbers 1-5 to their cubes
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
cubes = None  # TODO

# 2. From this list, create a dict mapping each word to its length
words = ["hello", "world", "python", "code"]
word_lengths = None  # TODO

# 3. Swap keys and values in this dictionary
original = {"a": 1, "b": 2, "c": 3}
swapped = None  # TODO: {1: "a", 2: "b", 3: "c"}

# Uncomment to test:
# print(f"\nCubes: {cubes}")
# print(f"Word lengths: {word_lengths}")
# print(f"Swapped: {swapped}")


# =============================================================================
# EXERCISE 6: Phonebook (CS50 classic!)
# =============================================================================
# TODO: Build a simple phonebook

phonebook = {}

# Add these contacts:
# - "Alice": "555-1234"
# - "Bob": "555-5678"
# - "Charlie": "555-9999"
# TODO

# Look up a contact (get Bob's number)
bobs_number = None  # TODO

# Check if "Diana" is in the phonebook
diana_exists = None  # TODO

# Print all contacts in format "Name: Number"
print("\nPhonebook:")
# TODO: Use a for loop

# Uncomment to test:
# print(f"\nBob's number: {bobs_number}")
# print(f"Diana exists: {diana_exists}")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Complete the exercises above!")
    print("="*50)
