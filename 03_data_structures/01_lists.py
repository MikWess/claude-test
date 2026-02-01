"""
Data Structures: Lists
======================
Learn about Python lists - ordered, mutable collections.
"""

# =============================================================================
# LESSON: Creating and accessing lists
# =============================================================================

fruits = ["apple", "banana", "cherry", "date"]

print("List:", fruits)
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Length: {len(fruits)}")

# Slicing
print(f"First two: {fruits[:2]}")
print(f"Last two: {fruits[-2:]}")
print(f"Middle: {fruits[1:3]}")


# =============================================================================
# EXERCISE 1: List basics
# =============================================================================
# TODO: Work with this list

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Get the third element
third = None  # TODO

# Get the last three elements
last_three = None  # TODO

# Get every other element (10, 30, 50, 70, 90)
every_other = None  # TODO: hint: use step in slice [::2]

# Reverse the list using slicing
reversed_nums = None  # TODO: hint: [::-1]

# Uncomment to test:
# print(f"\nThird element: {third}")
# print(f"Last three: {last_three}")
# print(f"Every other: {every_other}")
# print(f"Reversed: {reversed_nums}")


# =============================================================================
# LESSON: Modifying lists
# =============================================================================

colors = ["red", "green", "blue"]

# Adding items
colors.append("yellow")          # Add to end
colors.insert(1, "orange")       # Insert at index
colors.extend(["purple", "pink"]) # Add multiple

print(f"\nAfter adding: {colors}")

# Removing items
colors.remove("pink")    # Remove by value
popped = colors.pop()    # Remove and return last
del colors[0]            # Remove by index

print(f"After removing: {colors}")
print(f"Popped item: {popped}")


# =============================================================================
# EXERCISE 2: List modifications
# =============================================================================
# TODO: Modify this list

tasks = ["wake up", "eat breakfast", "go to work"]

# Add "exercise" to the end
# TODO

# Insert "shower" after "wake up" (index 1)
# TODO

# Remove "go to work"
# TODO

# Add ["lunch", "dinner"] to the end
# TODO

# Uncomment to test:
# print(f"\nModified tasks: {tasks}")
# Expected: ['wake up', 'shower', 'eat breakfast', 'exercise', 'lunch', 'dinner']


# =============================================================================
# LESSON: List operations
# =============================================================================

nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(f"\nOriginal: {nums}")
print(f"Sum: {sum(nums)}")
print(f"Min: {min(nums)}")
print(f"Max: {max(nums)}")
print(f"Count of 1s: {nums.count(1)}")
print(f"Index of 5: {nums.index(5)}")

# Sorting
sorted_nums = sorted(nums)       # Returns new sorted list
print(f"Sorted (new): {sorted_nums}")

nums_copy = nums.copy()
nums_copy.sort()                  # Sorts in place
print(f"Sorted (in place): {nums_copy}")


# =============================================================================
# EXERCISE 3: List operations
# =============================================================================
# TODO: Perform operations on this list

scores = [85, 92, 78, 95, 88, 72, 90, 85, 88, 95]

# Find the average score
average = None  # TODO: use sum() and len()

# Find how many times the top score appears
top_score = None  # TODO: use max()
top_count = None  # TODO: use count()

# Create a sorted list (highest to lowest)
sorted_scores = None  # TODO: hint: sorted(..., reverse=True)

# Uncomment to test:
# print(f"\nScores: {scores}")
# print(f"Average: {average:.1f}")
# print(f"Top score {top_score} appears {top_count} times")
# print(f"Sorted (desc): {sorted_scores}")


# =============================================================================
# LESSON: List comprehensions
# =============================================================================

# Traditional way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(f"\nSquares (loop): {squares}")

# List comprehension - same result, one line!
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares (comprehension): {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")


# =============================================================================
# EXERCISE 4: List comprehensions
# =============================================================================
# TODO: Create these lists using comprehensions

# 1. Cubes of numbers 1-10: [1, 8, 27, 64, ...]
cubes = None  # TODO

# 2. Numbers from 1-20 that are divisible by 3
div_by_3 = None  # TODO

# 3. Uppercase versions of these words
words = ["hello", "world", "python"]
uppercase_words = None  # TODO: hint: [w.upper() for w in words]

# 4. Lengths of each word
word_lengths = None  # TODO

# Uncomment to test:
# print(f"\nCubes: {cubes}")
# print(f"Divisible by 3: {div_by_3}")
# print(f"Uppercase: {uppercase_words}")
# print(f"Word lengths: {word_lengths}")


# =============================================================================
# EXERCISE 5: Practical list problems
# =============================================================================
# TODO: Solve these problems

grades = [88, 92, 75, 95, 89, 91, 78, 82, 96, 73]

# 1. Find all grades above 85
high_grades = None  # TODO: use list comprehension

# 2. Calculate how many students passed (grade >= 70)
passing_count = None  # TODO

# 3. Find the grade range (max - min)
grade_range = None  # TODO

# 4. Create a list of (grade, "Pass"/"Fail") tuples
# Example: [(88, "Pass"), (92, "Pass"), ...]
grade_status = None  # TODO: hint: [(g, "Pass" if g >= 70 else "Fail") for g in grades]

# Uncomment to test:
# print(f"\nGrades above 85: {high_grades}")
# print(f"Passing students: {passing_count}")
# print(f"Grade range: {grade_range}")
# print(f"Grade status: {grade_status}")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Complete the exercises above!")
    print("="*50)
