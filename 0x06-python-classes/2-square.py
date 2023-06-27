#!/usr/bin/python3
# 2-square.py by Harry Murrithi
""" Module that defines a square """


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

    def area(self):
        """
        calculates the area of the square

        Returns:
            square of the size
        """
        return self.__size ** 2
