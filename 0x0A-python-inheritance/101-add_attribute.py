#!/usr/bin/python3
"""
Module Doc: add attribute to custom object

Atrribute:
    obj (object): object to modify
    attr_name (str): name for new attribute
    attr_value (str): value for new attribite
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Function Doc: add attribute to object
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
