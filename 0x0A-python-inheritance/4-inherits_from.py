#!/usr/bin/python3
""" Module that defines an inherited class """


def inherits_from(obj, a_class):
    """
    Check if an object is an instance or object is an instance of a class

    Args:
        obj: The object to be checked
        a_class: The class to be compared against

    Returns:
        True if the object is an instance else return False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
