#!/usr/bin/python3
# 5-square.py by Harry Muriithi
""" Module that defines a square """


class Square:
    """ Class that represents a square """

    def __init__(self, size=0):
        """
        Initializes this square class
        Args:
            size: represents the defined size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than zero
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Retrives size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the square area
        Returns: The size of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ prints the square in # """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
