#!/usr/bin/python3
# 1-square.py by Harry Muriithi
""" Module that deines a square """


class Square:
    """
    Class that represents a square
    """
    def __init__(self, size=0):
        """
        Initialize a square object with an optional size.

        Args:
            size int: size of square defalult set to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
