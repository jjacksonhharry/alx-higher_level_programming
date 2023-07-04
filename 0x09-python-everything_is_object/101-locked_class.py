#!/usr/bin/python3
# 101-locked_class.py by Harry Muriithi
""" Module used to define a lockedclass """


class LockedClass:
    """
    Class that prevents the user from dynamically creating new instance attributes,
    except for the attribute 'first_name'

    Attributes:
        __slots__: A list specifying the allowed instance attributes.
    """
    __slots__ = ['first_name']
