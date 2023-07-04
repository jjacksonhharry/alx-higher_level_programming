#!/usr/bin/python3
""" Module defining locked class """


class LockedClass:
    """
    Class that prevents the user from dynamically creating new instance attributes,
    except for the attribute 'first_name'.
    """
    __slots__ = ['first_name']
