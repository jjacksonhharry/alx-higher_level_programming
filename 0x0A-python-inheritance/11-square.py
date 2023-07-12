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

    def __str__(self):
        """
        Return the string representation of the Square instance

        Returns:
            str: The string representation of the instance
        """
        return "[Square] {}/{}".format(
                self._Rectangle__width,
                self._Rectangle__height
                )
