#!/usr/bin/python3
""" Module defining a class inheritinh from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class representing a  rectangle using BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = 0
        self.__height = 0
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle

        Returns:
            int: The calculated area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the Rectangle instance

        Returns:
            str: The string representation of the instance
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
