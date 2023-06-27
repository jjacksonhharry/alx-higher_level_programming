#!/usr/bin/python3
# 3-square.py by Harry Muriithi
""" Module that defines a square """


class Square:
    """ A class representing a square """
    def __init__(self, size=0):
        """
        Initialize a square object

        Args:
            size: The size of the square defined

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculate the are of the square
        Returns: The square of the size
        """
        return (self.__size ** 2)
