"""
Mini Project 1: Password Generator
===================================
Combines: Functions, Loops, Strings, Random, User Input, Error Handling

Build a command-line password generator with various options.
"""

import random
import string

# =============================================================================
# TODO: Implement the password generator functions
# =============================================================================

def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_special=True, exclude_chars=""):
    """
    Generate a random password with the specified options.

    Args:
        length: Password length (minimum 4)
        use_uppercase: Include A-Z
        use_lowercase: Include a-z
        use_digits: Include 0-9
        use_special: Include !@#$%^&*()_+-=
        exclude_chars: Characters to exclude from password

    Returns:
        Generated password string

    Raises:
        ValueError: If no character types are selected or length < 4
    """
    # TODO: Implement this function
    # 1. Build the character pool based on options
    # 2. Remove excluded characters
    # 3. Ensure at least one character type is selected
    # 4. Generate random password of specified length
    # Bonus: Ensure at least one char of each selected type is included
    pass


def check_password_strength(password):
    """
    Check password strength and return a score.

    Scoring:
    - Length >= 8: +1
    - Length >= 12: +1
    - Length >= 16: +1
    - Has uppercase: +1
    - Has lowercase: +1
    - Has digits: +1
    - Has special chars: +1

    Returns:
        tuple: (score, strength_label, feedback)
        strength_label: "Weak", "Fair", "Good", "Strong", "Very Strong"
    """
    # TODO: Implement this function
    pass


def generate_passphrase(num_words=4, separator="-", capitalize=True):
    """
    Generate a passphrase using random words.

    Args:
        num_words: Number of words in passphrase
        separator: Character between words
        capitalize: Whether to capitalize each word

    Returns:
        Generated passphrase string
    """
    # Simple word list (in real app, use a larger dictionary file)
    words = [
        "apple", "banana", "cherry", "dragon", "elephant",
        "forest", "garden", "honey", "island", "jungle",
        "kitchen", "lemon", "mountain", "nature", "ocean",
        "planet", "quantum", "rainbow", "sunset", "thunder",
        "umbrella", "violet", "whisper", "xylophone", "yellow", "zebra",
        "crystal", "diamond", "emerald", "falcon", "glacier",
        "harbor", "ivory", "jasmine", "kingdom", "lantern"
    ]

    # TODO: Implement this function
    # 1. Select random words from the list
    # 2. Optionally capitalize each word
    # 3. Join with separator
    pass


def generate_pin(length=4):
    """Generate a numeric PIN."""
    # TODO: Implement this function
    pass


def generate_memorable_password():
    """
    Generate a memorable password in format: Word + Number + Word + Symbol
    Example: Blue42Tiger!
    """
    # TODO: Implement this function
    pass


# =============================================================================
# TODO: Implement the main CLI interface
# =============================================================================

def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("     PASSWORD GENERATOR")
    print("=" * 40)
    print("1. Generate Random Password")
    print("2. Generate Passphrase")
    print("3. Generate PIN")
    print("4. Generate Memorable Password")
    print("5. Check Password Strength")
    print("6. Exit")
    print("=" * 40)


def get_password_options():
    """Get password generation options from user."""
    # TODO: Implement this function
    # Ask for:
    # - Length
    # - Include uppercase? (y/n)
    # - Include lowercase? (y/n)
    # - Include digits? (y/n)
    # - Include special chars? (y/n)
    # - Characters to exclude
    # Return as dictionary
    pass


def main():
    """Main function to run the password generator."""
    print("Welcome to the Password Generator!")

    while True:
        show_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            # TODO: Get options and generate password
            # Display password and its strength
            pass

        elif choice == "2":
            # TODO: Get passphrase options and generate
            pass

        elif choice == "3":
            # TODO: Get PIN length and generate
            pass

        elif choice == "4":
            # TODO: Generate and display memorable password
            pass

        elif choice == "5":
            # TODO: Get password from user and check strength
            pass

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# =============================================================================
# Tests (uncomment to run)
# =============================================================================

def run_tests():
    """Test the password generator functions."""
    print("Running tests...")

    # Test generate_password
    pwd = generate_password(length=16)
    assert len(pwd) == 16, "Password length should be 16"
    print(f"✓ Generated password: {pwd}")

    # Test with only digits
    pwd_digits = generate_password(length=8, use_uppercase=False,
                                   use_lowercase=False, use_special=False)
    assert pwd_digits.isdigit(), "Should only contain digits"
    print(f"✓ Digits only: {pwd_digits}")

    # Test strength checker
    score, label, _ = check_password_strength("abc")
    assert label == "Weak", "Short password should be weak"
    print(f"✓ Weak password detected: score={score}")

    score, label, _ = check_password_strength("MySecure123!Password")
    assert label in ["Strong", "Very Strong"], "Strong password should be rated highly"
    print(f"✓ Strong password detected: score={score}")

    # Test passphrase
    phrase = generate_passphrase(num_words=4)
    assert len(phrase.split("-")) == 4, "Should have 4 words"
    print(f"✓ Generated passphrase: {phrase}")

    # Test PIN
    pin = generate_pin(6)
    assert len(pin) == 6 and pin.isdigit(), "PIN should be 6 digits"
    print(f"✓ Generated PIN: {pin}")

    print("\nAll tests passed!")


if __name__ == "__main__":
    # Uncomment to run tests:
    # run_tests()

    # Run the main program:
    main()
