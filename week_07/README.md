# Week 7: Working with Data Files

**Big Idea:** DAT (Data)

---

## Learning Objectives

By the end of this week, you should be able to:
- Read from and write to text files
- Work with CSV (comma-separated values) files
- Parse and create JSON data
- Understand data persistence

---

## AP CSP Concepts

### DAT-2: Data Processing
Programs often need to:
- **Read** data from files (input)
- **Process** data (transform, analyze)
- **Write** data to files (output, storage)

### Text Files
```python
# Writing to a file
with open("data.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Line 2\n")

# Reading from a file
with open("data.txt", "r") as f:
    content = f.read()      # Read entire file
    # or
    lines = f.readlines()   # Read as list of lines

# Appending to a file
with open("data.txt", "a") as f:
    f.write("New line\n")
```

### CSV Files
CSV is a common format for tabular data (spreadsheets).

```python
import csv

# Writing CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "NYC"])
    writer.writerow(["Bob", 30, "LA"])

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['Name', 'Age', 'City']

# Using DictReader (column names as keys)
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```

### JSON Files
JSON is common for structured data and APIs.

```python
import json

# Python dict to JSON
data = {"name": "Alice", "scores": [85, 90, 92]}
json_string = json.dumps(data)  # Convert to string

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON from file
with open("data.json", "r") as f:
    loaded = json.load(f)
```

### Data Formats Comparison
| Format | Best For | Structure |
|--------|----------|-----------|
| TXT | Simple text, logs | Unstructured |
| CSV | Tabular data, spreadsheets | Rows and columns |
| JSON | Nested data, APIs | Key-value pairs, nested |

---

## Practice Files

1. **01_text_files.py** - Reading and writing text files
2. **02_csv_json.py** - Working with structured data formats

---

## AP-Style Practice Questions

### Question 1
A program needs to store user preferences (name, theme color, font size). Which file format is most appropriate?
- A) Plain text (.txt)
- B) CSV
- C) JSON
- D) Binary

<details>
<summary>Answer</summary>
C) JSON — JSON is ideal for structured settings with key-value pairs
</details>

### Question 2
What is the output of this code?
```python
with open("test.txt", "w") as f:
    f.write("Line 1\n")
with open("test.txt", "w") as f:
    f.write("Line 2\n")
with open("test.txt", "r") as f:
    print(f.read())
```
- A) Line 1\nLine 2
- B) Line 2
- C) Line 1
- D) Error

<details>
<summary>Answer</summary>
B) Line 2 — The second "w" (write) mode overwrites the file
</details>

### Question 3
A dataset contains information about 10,000 students including their ID, name, grade level, and GPA. Which format would be most efficient for analyzing this data?
- A) Multiple text files, one per student
- B) A single CSV file
- C) A JSON file with nested objects
- D) A binary image file

<details>
<summary>Answer</summary>
B) A single CSV file — CSV is ideal for tabular data that can be easily analyzed
</details>

---

## Key Takeaways

1. Use `with` statements to properly handle file operations
2. Choose the right format: TXT for simple data, CSV for tables, JSON for structured data
3. "w" mode overwrites, "a" mode appends
4. Always close files (the `with` statement does this automatically)
5. Data persistence allows programs to save state between runs
