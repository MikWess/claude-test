"""
File I/O: Text Files
====================
Learn about reading and writing text files.
"""

import os

# Create a sample directory for our files
SAMPLE_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# LESSON: Writing to files
# =============================================================================

# Writing a file (creates or overwrites)
filepath = os.path.join(SAMPLE_DIR, "sample.txt")
with open(filepath, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

print(f"Created: {filepath}")


# Writing multiple lines at once
lines = ["Line A\n", "Line B\n", "Line C\n"]
filepath2 = os.path.join(SAMPLE_DIR, "lines.txt")
with open(filepath2, "w") as file:
    file.writelines(lines)

print(f"Created: {filepath2}")


# =============================================================================
# LESSON: Reading from files
# =============================================================================

# Read entire file
with open(filepath, "r") as file:
    content = file.read()
    print(f"\nFull content:\n{content}")

# Read line by line
print("Line by line:")
with open(filepath, "r") as file:
    for line in file:
        print(f"  {line.strip()}")  # strip() removes newline

# Read all lines into a list
with open(filepath, "r") as file:
    all_lines = file.readlines()
    print(f"\nAs list: {all_lines}")


# =============================================================================
# EXERCISE 1: Create a file
# =============================================================================
# TODO: Create a file with your information

# Create a file called "about_me.txt" in the sample directory
# Write at least 3 lines:
# - Your name
# - Your favorite programming language
# - What you want to build

about_me_path = os.path.join(SAMPLE_DIR, "about_me.txt")
# TODO: Write the file


# =============================================================================
# EXERCISE 2: Read and process a file
# =============================================================================
# TODO: Read the file and process it

# Read "sample.txt" and:
# 1. Count the number of lines
# 2. Count the total number of characters (excluding newlines)
# 3. Find the longest line

line_count = None  # TODO
char_count = None  # TODO
longest_line = None  # TODO

# Uncomment to test:
# print(f"\nLines: {line_count}")
# print(f"Characters: {char_count}")
# print(f"Longest line: '{longest_line}'")


# =============================================================================
# LESSON: Appending to files
# =============================================================================

# Append mode - adds to end of file
with open(filepath, "a") as file:
    file.write("This line was appended!\n")

print("\nAfter appending:")
with open(filepath, "r") as file:
    print(file.read())


# =============================================================================
# EXERCISE 3: Log file
# =============================================================================
# TODO: Create a simple logging system

from datetime import datetime

log_path = os.path.join(SAMPLE_DIR, "activity.log")

def log_message(message):
    """Append a timestamped message to the log file."""
    # TODO: Open file in append mode
    # Write: "[TIMESTAMP] message\n"
    # Hint: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pass

def read_log():
    """Read and return all log entries."""
    # TODO: Return the contents of the log file
    # Return empty string if file doesn't exist
    pass

# Uncomment to test:
# log_message("Application started")
# log_message("User logged in")
# log_message("Data saved")
# print("\nLog contents:")
# print(read_log())


# =============================================================================
# EXERCISE 4: Word counter
# =============================================================================
# TODO: Count word frequencies in a file

sample_text_path = os.path.join(SAMPLE_DIR, "sample_text.txt")

# First, create a sample text file
sample_text = """Python is a great programming language.
Python is easy to learn.
Programming in Python is fun.
Many developers love Python for its simplicity."""

with open(sample_text_path, "w") as f:
    f.write(sample_text)

def count_words(filepath):
    """
    Count word frequencies in a file.
    Returns a dictionary: {word: count}
    """
    # TODO:
    # 1. Read the file
    # 2. Convert to lowercase
    # 3. Split into words
    # 4. Count each word
    # Hint: Use a dictionary
    pass

# Uncomment to test:
# word_counts = count_words(sample_text_path)
# print("\nWord frequencies:")
# for word, count in sorted(word_counts.items(), key=lambda x: -x[1])[:5]:
#     print(f"  {word}: {count}")


# =============================================================================
# EXERCISE 5: File search
# =============================================================================
# TODO: Search for a pattern in a file

def search_file(filepath, pattern):
    """
    Search for a pattern in a file.
    Returns list of (line_number, line_content) tuples where pattern was found.
    """
    # TODO:
    # 1. Read file line by line
    # 2. Check if pattern is in each line (case-insensitive)
    # 3. Return list of matches with line numbers
    pass

# Uncomment to test:
# matches = search_file(sample_text_path, "python")
# print(f"\nLines containing 'python':")
# for line_num, line in matches:
#     print(f"  Line {line_num}: {line.strip()}")


# =============================================================================
# Cleanup helper (run at end)
# =============================================================================
def cleanup_files():
    """Remove sample files created during exercises."""
    files_to_remove = [
        "sample.txt", "lines.txt", "about_me.txt",
        "activity.log", "sample_text.txt"
    ]
    for filename in files_to_remove:
        path = os.path.join(SAMPLE_DIR, filename)
        if os.path.exists(path):
            os.remove(path)
            print(f"Removed: {filename}")

# Uncomment to clean up:
# cleanup_files()


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Complete the exercises above!")
    print("="*50)
