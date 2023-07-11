#!/usr/bin/python3
""" Module representing a function that inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line

    Args:
        filename: Name of the file
        search_string: The string to search for
        new_string: Line of text to insert
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
