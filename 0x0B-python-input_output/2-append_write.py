#!/usr/bin/python3
""" writes  a function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and return number of chars
    """
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
