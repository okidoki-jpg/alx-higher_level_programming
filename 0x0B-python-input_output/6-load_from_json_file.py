#!/usr/bin/python3
import json

"""
Module Doc: Create object from JSON file

Attributes:
    filene (str): path to file

Return:
    Object from JSON file
"""


def load_from_json_file(filename):
    """
    Function Doc: Return object from JSON file
    """

    with open(filename, "r") as file:
        return json.load(file)
