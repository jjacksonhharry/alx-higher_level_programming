#!/usr/bin/python3
""" Module of my int inheriting from int """


class MyInt(int):
    """ class representing MyInt that inherits from int """

    def __eq__(self, value):
        """
        Implement the inverted equality operator

        Args:
            value: The object to compare with

        Returns:
            bool: True if the values are not equal, False otherwise
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """
        Implement the inverted inequality operator

        Args:
            value: The object to compare with

        Returns:
            True if the values are equal, False otherwise
        """
        return super().__eq__(value)
