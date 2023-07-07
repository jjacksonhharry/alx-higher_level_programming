#!/usr/bin/python3
# 4-print_square.py by Harry Muriithi
""" Module that defines a square """


def print_square(size):
    """
    Prints a square with the character '#' of the given size

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer or a float.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print ("#" * size)
