#!/usr/bin/python3
""" Module that defines a class BaseGeometry """


class BaseGeometry:
    """
    Class representing BaseGeometry
    """

    def area(self):
        """
        Calculates the area of the geometry

        Raises:
            Exception: Indicates that the method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value

        Args:
            name: Name of the value
            value: Value to be validated

        Rasies:
            TypeError: Indicates that the value is not an integer
            ValueError: Indicates that the value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
