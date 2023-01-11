#!/usr/bin/python3
"""
Module Doc: Return JSON representation of object

Attributes:
    my_obj (object): object to represent

Return:
    JSON representation of object
"""


import json


def to_json_string(my_obj):
    """
    Function Doc: return JSON representation of my_obj
    """

    return json.dumps(my_obj)
