#!/usr/bin/python3
"""
Module Doc: add items from sys args to list and write it to json file

Attributes:
    args (any object): sys args
"""


import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


def add_item(args):
    """
    Function Doc: add sys args to list & wrute them to json file
    """

    """
    load/create new list
    """
    try:
        my_list = load("add_items.json")
    except Exception as e:
        my_list = []

    """
    add items to list
    """
    for item in args:
        my_list.append(item)

    """
    save new list
    """
    save(my_list, "add_items.json")


add_item(sys.argv[1:])
