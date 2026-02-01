"""
Libraries: External Packages
============================
Learn about using external Python packages.
"""

# =============================================================================
# LESSON: Importing modules
# =============================================================================

# Built-in modules (no installation needed)
import random
import datetime
import os
import math

# Different import styles
from datetime import date, timedelta
from math import pi, sqrt

print("=== Built-in Modules ===")
print(f"Random number (1-10): {random.randint(1, 10)}")
print(f"Today: {date.today()}")
print(f"Pi: {pi:.4f}")
print(f"Square root of 16: {sqrt(16)}")


# =============================================================================
# EXERCISE 1: Random module
# =============================================================================
# TODO: Use the random module

# Generate a random password of 8 characters
# Use: random.choice() and string module
import string

def generate_password(length=8):
    """Generate a random password with letters and digits."""
    # TODO:
    # characters = string.ascii_letters + string.digits
    # Use random.choice() in a loop or list comprehension
    pass

# Roll a dice (1-6)
def roll_dice():
    """Return a random number 1-6."""
    # TODO
    pass

# Shuffle a list
def shuffle_list(items):
    """Return a shuffled copy of the list."""
    # TODO: Use random.shuffle() (careful - it modifies in place!)
    pass

# Uncomment to test:
# print(f"\nRandom password: {generate_password()}")
# print(f"Dice roll: {roll_dice()}")
# print(f"Shuffled [1,2,3,4,5]: {shuffle_list([1,2,3,4,5])}")


# =============================================================================
# EXERCISE 2: Datetime module
# =============================================================================
# TODO: Work with dates and times

def days_until_birthday(month, day):
    """
    Calculate days until next birthday.
    If birthday has passed this year, calculate for next year.
    """
    # TODO:
    # Get today's date
    # Create date for birthday this year
    # If birthday passed, use next year
    # Return difference in days
    pass

def format_date(date_obj, style="long"):
    """
    Format a date object.
    style="long": "January 15, 2024"
    style="short": "01/15/24"
    style="iso": "2024-01-15"
    """
    # TODO: Use strftime()
    # %B = full month, %d = day, %Y = full year, %y = 2-digit year, %m = month number
    pass

def add_business_days(start_date, num_days):
    """
    Add business days (skip weekends) to a date.
    """
    # TODO:
    # Loop through days
    # Only count Mon-Fri (weekday() returns 0-4 for Mon-Fri)
    pass

# Uncomment to test:
# print(f"\nDays until July 4th: {days_until_birthday(7, 4)}")
# today = date.today()
# print(f"Long format: {format_date(today, 'long')}")
# print(f"Short format: {format_date(today, 'short')}")
# print(f"ISO format: {format_date(today, 'iso')}")


# =============================================================================
# LESSON: Installing external packages
# =============================================================================

# To install a package: pip install package_name
# Example: pip install requests

# Note: Run these in your terminal, not in Python!
# pip install requests
# pip install qrcode
# pip install pillow


# =============================================================================
# EXERCISE 3: Requests library (if installed)
# =============================================================================
# TODO: Make HTTP requests

# Note: This requires 'pip install requests'
# Skip this exercise if you haven't installed it

def fetch_json(url):
    """
    Fetch JSON data from a URL.
    Returns the parsed JSON or None if request fails.
    """
    try:
        import requests
        # TODO:
        # Make GET request
        # Check response.status_code == 200
        # Return response.json()
        pass
    except ImportError:
        print("requests not installed. Run: pip install requests")
        return None

def get_random_joke():
    """Fetch a random joke from an API."""
    # TODO: Use https://official-joke-api.appspot.com/random_joke
    pass

# Uncomment to test (requires internet + requests):
# joke = get_random_joke()
# if joke:
#     print(f"\nJoke: {joke.get('setup')}")
#     print(f"Punchline: {joke.get('punchline')}")


# =============================================================================
# EXERCISE 4: QR Code generator (if installed)
# =============================================================================
# TODO: Generate QR codes

# Note: This requires 'pip install qrcode pillow'

def create_qr_code(data, filename="qrcode.png"):
    """
    Generate a QR code image.
    """
    try:
        import qrcode
        # TODO:
        # qr = qrcode.QRCode(version=1, box_size=10, border=5)
        # qr.add_data(data)
        # qr.make(fit=True)
        # img = qr.make_image(fill_color="black", back_color="white")
        # img.save(filename)
        pass
    except ImportError:
        print("qrcode not installed. Run: pip install qrcode pillow")

# Uncomment to test (requires qrcode + pillow):
# create_qr_code("https://github.com/MikWess", "my_github.png")
# print("QR code created!")


# =============================================================================
# EXERCISE 5: Create a utility module
# =============================================================================
# TODO: Create your own reusable utility functions

def slugify(text):
    """
    Convert text to a URL-friendly slug.
    "Hello World!" -> "hello-world"
    """
    # TODO:
    # Convert to lowercase
    # Replace spaces with hyphens
    # Remove non-alphanumeric characters (except hyphens)
    pass

def truncate(text, max_length, suffix="..."):
    """
    Truncate text to max_length, adding suffix if truncated.
    "Hello World" with max_length=8 -> "Hello..."
    """
    # TODO
    pass

def chunk_list(lst, chunk_size):
    """
    Split a list into chunks of specified size.
    [1,2,3,4,5] with chunk_size=2 -> [[1,2], [3,4], [5]]
    """
    # TODO
    pass

# Uncomment to test:
# print(f"\nSlugify 'Hello World!': {slugify('Hello World!')}")
# print(f"Truncate 'Hello World' to 8: {truncate('Hello World', 8)}")
# print(f"Chunk [1,2,3,4,5] by 2: {chunk_list([1,2,3,4,5], 2)}")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Complete the exercises above!")
    print("="*50)
