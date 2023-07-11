#!/usr/bin/python3
""" Module defining a function that reads a text file (UTF8) and prints it """


def read_file(filename=""):
    """
    Read the contents of a text file and print them to stdout
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
