#!/usr/bin/python3
""" Module that defines a class checking function """


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of specified class

    Returns True if it is else return False
    """
    return type(obj) is a_class
