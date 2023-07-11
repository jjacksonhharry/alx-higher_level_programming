#!/usr/bin/python3
""" Module defining a function that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename: The name of the JSON file

    Returns:
        The object created from the JSON file
    """
    with open(filename) as file:
        return json.load(file)
