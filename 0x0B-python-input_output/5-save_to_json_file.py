#!/usr/bin/python3
""" Module that writes a function that writes an Object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes an object to JSON and writes it to a text file

    Args:
        my_obj: The object to be serialized and saved
        filename: The name of the file to save the JSON representation to
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
