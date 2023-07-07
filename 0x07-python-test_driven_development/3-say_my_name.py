#!/usr/bin/python3
# 3-say_my_name.py by Harry Muriithi
""" Module that defines print function """


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
