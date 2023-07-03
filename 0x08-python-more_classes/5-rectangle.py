#!/usr/bin/python3
# 5-rectangle.py by Harry Muriithi
""" Module that defines a rectangle """


class Rectangle:
    """ Class representing a rectangle """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle class

        Args:
            width: representing the width of the rectangle
            height: representing the height of the rectangle

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

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate and return the perimeter of the rectangle """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for _ in range(self.__height):
            rectangle += "#" * self.__width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """ Return a string representation of the rectangle object """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Print a message when an instance of Rectangle is deleted """
        print("Bye rectangle...")
