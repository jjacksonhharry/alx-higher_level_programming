#!/usr/bin/python3
""" Module defining a function that returns the dictionary for JSON """


def class_to_json(obj):
    """
    Returns a dictionary description for JSON

    Args:
        obj: The object to convert to a dictionary

    Returns:
        A dictionary representation of the object
    """
    return obj.__dict__
