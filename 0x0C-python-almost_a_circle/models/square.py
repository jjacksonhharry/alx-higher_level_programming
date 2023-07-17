#!/usr/bin/python3
""" Module representing a class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance

        Args:
            size (int): Size of the square
            x: x-coordinate of the square
            y: y-coordinate of the square
            id: Unique identifier for the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Set attribute for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Assigns attributes based on arguments and keyword arguments
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if len(args) == 0 or len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
