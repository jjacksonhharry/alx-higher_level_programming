#!/usr/bin/python3
""" module that defines a subclass Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class representing a square """

    def __init__(self, size):
        """
        Initialize a new Square

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
