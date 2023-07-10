#!/usr/bin/python3
""" Module defining a function that adds a new attribute """


def add_attribute(obj, attribute, value):
    """
    function that adds a new attribute to an object

    Args:
        obj: The object to add attribute
        attribute: The name of the attribute
        value: The value to assign the attribute
    Raise:
        TypeError: If the object can't have new attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
