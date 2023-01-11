#!/usr/bin/python3
import json

"""
Module Doc: Write JSON represented object to text file

Attributes:
    my_obj (object): object to write
    filename (str) : patg to file
"""

def save_to_json_file(my_obj, filename):
    """
    Function Doc: Write JSON represented object to text file
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
