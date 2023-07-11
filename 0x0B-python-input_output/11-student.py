#!/usr/bin/python3
""" Module defining a class Student that defines a student """


class Student:
    """ class representing a student """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs: A list of attribute names to retrieve
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
                    }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values

        Args:
            json: A dictionary containing attribute names
        """
        for key, value in json.items():
            setattr(self, key, value)
