#!/usr/bin/python3
""" Defines a function that writes a string to a text file """


def write_file(filename="", text=""):
    """
    Write a string to a text file and return number of characters

    Args:
        filename (str): The name of the file to write the text
        text (str): The string to be written to the file

    Returns:
        int: The number of characters written to file
    """
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
