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

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return self.__dict__
