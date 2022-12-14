#!/usr/bin/python3
"""
Module Doc: Return an object represented by a JSON str

Attributes:
    my_str (str): objecct to represent

Return:
    JSON string of obj
"""


import json


def from_json_string(my_str):
    """
    Function Doc: Return JSON string representation of my_str
    """

    return json.loads(my_str)
