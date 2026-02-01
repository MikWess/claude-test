"""
Control Flow: Loops
===================
Learn about for loops, while loops, and loop control.
"""

# =============================================================================
# LESSON: for loops with range()
# =============================================================================

print("Counting 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

print("\nCounting 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

print("\nCounting by 2s (0 to 10):")
for i in range(0, 11, 2):
    print(i, end=" ")
print()


# =============================================================================
# EXERCISE 1: Number patterns
# =============================================================================
# TODO: Print the following patterns using for loops

# Pattern 1: Print numbers 10, 9, 8, ... 1 (countdown)
print("\nCountdown:")
# TODO: Write a for loop (hint: range can count backwards!)


# Pattern 2: Print multiples of 3 from 3 to 30
print("\nMultiples of 3:")
# TODO: Write a for loop


# Pattern 3: Print 1, 4, 9, 16, 25 (squares of 1-5)
print("\nSquares:")
# TODO: Write a for loop


# =============================================================================
# LESSON: for loops with lists
# =============================================================================

fruits = ["apple", "banana", "cherry"]

print("\nIterating over list:")
for fruit in fruits:
    print(f"I like {fruit}")

print("\nWith index (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# =============================================================================
# EXERCISE 2: List iteration
# =============================================================================
# TODO: Work with this list

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Print each name with its length
# Example output: "Alice has 5 letters"
print("\nName lengths:")
# TODO: Write a for loop


# Print only names that start with a vowel (A, E, I, O, U)
print("\nNames starting with vowels:")
# TODO: Write a for loop with an if condition


# =============================================================================
# LESSON: while loops
# =============================================================================

print("\nWhile loop counting to 5:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print()


# =============================================================================
# EXERCISE 3: while loops
# =============================================================================
# TODO: Complete these while loop exercises

# Exercise: Sum numbers until total exceeds 100
# Start with total = 0, add 1, then 2, then 3... until total > 100
# Print how many numbers you added

total = 0
num = 0
# TODO: Write a while loop

# Uncomment when ready:
# print(f"\nAdded {num} numbers to get total of {total}")


# =============================================================================
# LESSON: break and continue
# =============================================================================

print("\nUsing break (stop at 5):")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

print("\nUsing continue (skip evens):")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()


# =============================================================================
# EXERCISE 4: Loop control
# =============================================================================
# TODO: Use break and continue

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

# Print numbers until you hit an even number, then stop
print("\nPrint until even (use break):")
# TODO


# Print all numbers, but skip multiples of 3
print("\nSkip multiples of 3 (use continue):")
# TODO


# =============================================================================
# LESSON: Nested loops
# =============================================================================

print("\nMultiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()


# =============================================================================
# EXERCISE 5: Mario pyramid (CS50 classic!)
# =============================================================================
# TODO: Print a pyramid of # characters

# For height = 4, output should be:
#    #
#   ##
#  ###
# ####

height = 4

print("\nMario pyramid:")
# TODO: Use nested loops
# Hint: For each row, print (height - row - 1) spaces, then (row + 1) hashes


# =============================================================================
# EXERCISE 6: Find prime numbers
# =============================================================================
# TODO: Print all prime numbers between 2 and 30

# A prime number is only divisible by 1 and itself

print("\nPrime numbers (2-30):")
# TODO: Use nested loops and break
# Hint: For each number n, check if any number from 2 to n-1 divides it evenly


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Complete the exercises above!")
    print("="*50)
