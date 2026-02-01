"""
File I/O: CSV and JSON
======================
Learn about structured data formats.
"""

import csv
import json
import os

SAMPLE_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================================
# LESSON: Writing CSV files
# =============================================================================

csv_path = os.path.join(SAMPLE_DIR, "students.csv")

# Writing with csv.writer
students_data = [
    ["name", "age", "grade"],
    ["Alice", 20, "A"],
    ["Bob", 21, "B"],
    ["Charlie", 19, "A"]
]

with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print(f"Created: {csv_path}")

# Writing with csv.DictWriter (more readable!)
dict_csv_path = os.path.join(SAMPLE_DIR, "students_dict.csv")

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

with open(dict_csv_path, "w", newline="") as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print(f"Created: {dict_csv_path}")


# =============================================================================
# LESSON: Reading CSV files
# =============================================================================

print("\nReading with csv.reader:")
with open(csv_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"  {row}")

print("\nReading with csv.DictReader:")
with open(dict_csv_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"  {row['name']} is {row['age']} years old, grade: {row['grade']}")


# =============================================================================
# EXERCISE 1: Create and read a CSV
# =============================================================================
# TODO: Create a CSV file for a product inventory

products_path = os.path.join(SAMPLE_DIR, "products.csv")

# Create a CSV with columns: product, price, quantity
# Add at least 4 products
# TODO: Write the CSV using DictWriter


# Read the CSV and calculate total inventory value (price * quantity for each)
total_value = 0
# TODO: Read the CSV and calculate


# Uncomment to test:
# print(f"\nTotal inventory value: ${total_value:.2f}")


# =============================================================================
# LESSON: JSON basics
# =============================================================================

# Python dict <-> JSON
data = {
    "name": "Alice",
    "age": 25,
    "languages": ["Python", "JavaScript"],
    "is_developer": True,
    "address": {
        "city": "Boston",
        "country": "USA"
    }
}

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print(f"\nJSON string:\n{json_string}")

# Convert back to Python dict
parsed_data = json.loads(json_string)
print(f"\nParsed name: {parsed_data['name']}")


# =============================================================================
# LESSON: Reading and writing JSON files
# =============================================================================

json_path = os.path.join(SAMPLE_DIR, "config.json")

# Write JSON file
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "features": ["login", "dashboard", "reports"]
}

with open(json_path, "w") as file:
    json.dump(config, file, indent=2)

print(f"\nCreated: {json_path}")

# Read JSON file
with open(json_path, "r") as file:
    loaded_config = json.load(file)

print(f"Loaded config: {loaded_config['app_name']} v{loaded_config['version']}")


# =============================================================================
# EXERCISE 2: JSON configuration
# =============================================================================
# TODO: Create a settings manager

settings_path = os.path.join(SAMPLE_DIR, "settings.json")

def save_settings(settings):
    """Save settings dictionary to JSON file."""
    # TODO
    pass

def load_settings():
    """Load settings from JSON file. Return empty dict if file doesn't exist."""
    # TODO: Handle file not found
    pass

def update_setting(key, value):
    """Update a single setting and save."""
    # TODO: Load, update, save
    pass

# Uncomment to test:
# save_settings({"theme": "dark", "font_size": 14, "notifications": True})
# print(f"\nLoaded settings: {load_settings()}")
# update_setting("font_size", 16)
# print(f"After update: {load_settings()}")


# =============================================================================
# EXERCISE 3: Contact book (JSON)
# =============================================================================
# TODO: Build a contact book using JSON storage

contacts_path = os.path.join(SAMPLE_DIR, "contacts.json")

def load_contacts():
    """Load contacts from file. Return empty dict if file doesn't exist."""
    # TODO
    pass

def save_contacts(contacts):
    """Save contacts to file."""
    # TODO
    pass

def add_contact(name, phone, email):
    """Add a new contact."""
    # TODO: Load contacts, add new one, save
    pass

def find_contact(name):
    """Find a contact by name (case-insensitive)."""
    # TODO
    pass

def list_contacts():
    """Print all contacts."""
    # TODO
    pass

# Uncomment to test:
# add_contact("Alice", "555-1234", "alice@email.com")
# add_contact("Bob", "555-5678", "bob@email.com")
# add_contact("Charlie", "555-9999", "charlie@email.com")
# print("\nAll contacts:")
# list_contacts()
# print(f"\nFind 'alice': {find_contact('alice')}")


# =============================================================================
# EXERCISE 4: CSV to JSON converter
# =============================================================================
# TODO: Convert CSV data to JSON format

def csv_to_json(csv_filepath, json_filepath):
    """
    Convert a CSV file to a JSON file.
    Each row becomes an object in a JSON array.
    """
    # TODO:
    # 1. Read CSV using DictReader
    # 2. Convert to list of dictionaries
    # 3. Write as JSON
    pass

def json_to_csv(json_filepath, csv_filepath):
    """
    Convert a JSON file (array of objects) to CSV.
    Assumes all objects have the same keys.
    """
    # TODO:
    # 1. Read JSON
    # 2. Get fieldnames from first object
    # 3. Write CSV using DictWriter
    pass

# Uncomment to test:
# csv_to_json(dict_csv_path, os.path.join(SAMPLE_DIR, "students.json"))
# print("\nConverted CSV to JSON")
# with open(os.path.join(SAMPLE_DIR, "students.json"), "r") as f:
#     print(f.read())


# =============================================================================
# Cleanup
# =============================================================================
def cleanup_files():
    """Remove sample files."""
    files = [
        "students.csv", "students_dict.csv", "products.csv",
        "config.json", "settings.json", "contacts.json", "students.json"
    ]
    for filename in files:
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
