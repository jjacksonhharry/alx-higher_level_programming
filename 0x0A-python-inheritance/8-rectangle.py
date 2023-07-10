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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
