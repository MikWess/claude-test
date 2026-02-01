"""
Week 2: Data Representation Practice
=====================================
Big Idea: DAT (Data)

Understanding how computers store and represent data.
"""

# =============================================================================
# Binary Conversion Examples
# =============================================================================

def binary_examples():
    """Demonstrate binary conversion in Python."""
    # Decimal to Binary
    print("Decimal to Binary:")
    for num in [5, 10, 15, 100, 255]:
        binary = bin(num)
        print(f"  {num} = {binary} = {binary[2:]}")  # [2:] removes '0b' prefix

    print("\nBinary to Decimal:")
    for binary_str in ['101', '1010', '1111', '11111111']:
        decimal = int(binary_str, 2)
        print(f"  {binary_str} = {decimal}")


# =============================================================================
# TODO: Exercise 1 - Manual Binary to Decimal
# =============================================================================

def binary_to_decimal(binary_string):
    """
    Convert a binary string to decimal WITHOUT using int().
    Use the positional value method.

    Example: '1101' = 1×8 + 1×4 + 0×2 + 1×1 = 13

    Args:
        binary_string: A string of 0s and 1s (e.g., "1101")

    Returns:
        The decimal (base 10) value
    """
    # TODO: Implement using a loop
    # Hint: Start from the right, multiply each digit by its positional value
    pass


# =============================================================================
# TODO: Exercise 2 - Decimal to Binary
# =============================================================================

def decimal_to_binary(decimal_num):
    """
    Convert a decimal number to binary string WITHOUT using bin().
    Use repeated division by 2.

    Example: 13 → 1101
        13 ÷ 2 = 6 remainder 1
        6 ÷ 2 = 3 remainder 0
        3 ÷ 2 = 1 remainder 1
        1 ÷ 2 = 0 remainder 1
        Read remainders bottom-up: 1101

    Args:
        decimal_num: A positive integer

    Returns:
        Binary representation as a string
    """
    # TODO: Implement using repeated division
    pass


# =============================================================================
# TODO: Exercise 3 - Character Codes
# =============================================================================

def explore_ascii():
    """
    Print the ASCII values for:
    1. Uppercase letters A-Z
    2. Lowercase letters a-z
    3. Digits 0-9

    Example output:
        A = 65, B = 66, C = 67, ...
    """
    # TODO: Use ord() and loops to explore ASCII values
    pass


# =============================================================================
# TODO: Exercise 4 - Bit Counter
# =============================================================================

def count_bits(number):
    """
    Count how many bits are needed to represent a number in binary.

    Examples:
        count_bits(1) → 1  (binary: 1)
        count_bits(5) → 3  (binary: 101)
        count_bits(100) → 7  (binary: 1100100)

    Args:
        number: A positive integer

    Returns:
        Number of bits needed
    """
    # TODO: Implement (hint: you can use your decimal_to_binary function)
    pass


# =============================================================================
# TODO: Exercise 5 - Overflow Simulation
# =============================================================================

def simulate_overflow(value, bits=8):
    """
    Simulate what happens when a value overflows in a fixed-bit system.

    In an 8-bit system, values 0-255 are valid.
    If you add 1 to 255, you get 0 (overflow/wraparound).

    Args:
        value: The value to store
        bits: Number of bits in the system (default 8)

    Returns:
        The actual stored value after potential overflow

    Examples:
        simulate_overflow(200, 8) → 200  (fits in 8 bits)
        simulate_overflow(300, 8) → 44   (300 mod 256 = 44)
        simulate_overflow(256, 8) → 0    (wraps around)
    """
    # TODO: Implement using modulo operator
    pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    """Test the exercises."""
    print("Running tests...\n")

    # Test binary_to_decimal
    if binary_to_decimal:
        assert binary_to_decimal('1101') == 13, "1101 should be 13"
        assert binary_to_decimal('1010') == 10, "1010 should be 10"
        assert binary_to_decimal('11111111') == 255, "11111111 should be 255"
        print("✓ binary_to_decimal tests passed")

    # Test decimal_to_binary
    if decimal_to_binary:
        assert decimal_to_binary(13) == '1101', "13 should be 1101"
        assert decimal_to_binary(10) == '1010', "10 should be 1010"
        print("✓ decimal_to_binary tests passed")

    # Test count_bits
    if count_bits:
        assert count_bits(1) == 1
        assert count_bits(5) == 3
        assert count_bits(100) == 7
        print("✓ count_bits tests passed")

    # Test simulate_overflow
    if simulate_overflow:
        assert simulate_overflow(200, 8) == 200
        assert simulate_overflow(300, 8) == 44
        assert simulate_overflow(256, 8) == 0
        print("✓ simulate_overflow tests passed")

    print("\nAll tests passed!")


if __name__ == "__main__":
    print("=" * 50)
    print("Week 2: Data Representation")
    print("=" * 50)

    # Show examples
    binary_examples()

    # Uncomment to run tests after implementing:
    # run_tests()
