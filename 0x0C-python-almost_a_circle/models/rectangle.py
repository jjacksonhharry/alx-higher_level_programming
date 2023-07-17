#!/usr/bin/python3
""" Module defining a class rectangle """
from models.base import Base


class Rectangle(Base):
    """Class Representing a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance

        Args:
            width: Width of the rectangle
            height: Height of the rectangle
            x: x-coordinate of the rectangle
            y: y-coordinate of the rectangle
            id: Unique identifier for the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width attribute

        Args:
            value: size to assign to width

        Raises:
            TypeError: Width must be an integer
            ValueError: Width must be > 0
        """
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height attribute

        Args:
            value: size to assign to height

        Raises:
            TypeError: Height must be an integer
            ValueError: Height must be > 0
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        elif value <= 0:
            raise ValueError("Height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter fo x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x attribute

        Args:
            value: size to assign to x

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets rhe y attribute

        Args:
            value: size to assign to y

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise ValueError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Method that calculates and returns area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rectangle with '#' to stdout
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Method that overides the str method
        """
        return (
                f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
                )

    def update(self, *args, **kwargs):
        """
        assigns arguments to the attributes
        """
        if len(args) > 0:
            self.id = args[0]

        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
