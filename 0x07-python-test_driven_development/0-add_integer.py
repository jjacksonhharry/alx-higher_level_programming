#!/usr/bin/python3
# 0-add_integer.py by Harry Muriithi
""" Module that has the addition function """


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int or float): The 1st number
        b (int or float): The 2nd number

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
