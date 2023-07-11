#!/usr/bin/python3
""" writes a function that returns an object (Python data structure) """
import json


def from_json_string(my_str):
    """
    Return an object represented by a JSON string

    Args:
        my_str (str): The JSON string to be converted to an object

    Returns:
        object: The Python data structure represented by the JSON string
    """
    return json.loads(my_str)
