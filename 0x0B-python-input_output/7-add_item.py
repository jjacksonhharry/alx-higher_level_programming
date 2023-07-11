#!/usr/bin/python3
""" Module containing function that adds arguments to a list """


import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if exists(filename):
    try:
        my_list = load_from_json_file(filename)
    except ValueError:
        my_list = []
else:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)
