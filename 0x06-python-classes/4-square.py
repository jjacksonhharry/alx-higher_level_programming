#!/usr/bin/python3
# 4-square.py by Harry Muriithi
""" Module that defines a square """


class Square:
    """ Class representing a square """
    def __init__(self, size=0):
        """Initializes the square class

        Args:
            size: representing the size of square

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Retrives the size of the square """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates the area of the square
        Returns:The area of the square
        """
        return (self.__size ** 2)
