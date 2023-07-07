#!/usr/bin/python3
# 5-text_indentation.py by Harry Muriithi
""" Module that defines a function that prints a text with 2 new lines """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'

    Args:
        text (str): The text to be indented

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    result = []
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line:
            for char in line:
                result.append(char)
                if char in punctuations:
                    result.append("\n\n")
        else:
            result.append("\n\n")

    print("".join(result))
