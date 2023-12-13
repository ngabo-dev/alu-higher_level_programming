#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b, both casted to integers.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    # Check if both a and b are either integers or floats
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the sum of a and b
    return a + b

# Example usage:
result = add_integer(5, 3.5)
print(result)  # Output: 8

result = add_integer(10)
print(result)  # Output: 108

# TypeError in action:
#result = add_integer("string", 5)
#print(result)
