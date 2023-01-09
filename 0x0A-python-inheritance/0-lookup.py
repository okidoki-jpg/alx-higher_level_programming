#!/usr/bin/python3
"""
lookup module: return object attributes

Attributes:
    obj (class object): class obj to analyze

Return:
    list of class attributes
"""


def lookup(obj):

    """
    Return list of object attributes
    """
    return (dir(obj))
