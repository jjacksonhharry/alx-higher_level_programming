#!/usr/bin/python3
# 1-rectangle.py by Harry Muriithi
""" Module that defines a rectangle """


class Rectangle:
    """ Class representing a rectangle """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle class

        Args:
            height: representing the height of the rectangle
            width: representing the width of the rectangle

        Raises:
            TypeError: if size is not an integer
            ValueError: ifsize is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the weight attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
