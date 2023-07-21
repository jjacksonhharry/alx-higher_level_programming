#!/usr/bin/python3
""" Module that defines a class base """
import json
import csv


class Base:
    """ Base class representing a base model """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a base instance

        Args:
            id (int): Unique identifier for instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            obj_dicts = []

        json_string = cls.to_json_string(obj_dicts)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by the JSON string
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                data = file.read()
                if data:
                    instance_list = cls.from_json_string(data)
                    return [cls.create(**obj_dict) for obj_dict in instance_list]
                else:
                    return []
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serialize object to a CSV file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as file:
            if cls.__name__ == 'Rectangle':
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes objects from a CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fieldnames = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(file, fieldnames=fieldnames)
                instances = []
                for row in reader:
                    row = {k: int(v) for k, v in row.items()}

                    instance = cls.create(**row)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
