#!/usr/bin/python3
"""
Module Doc: is_same_class
determine if object is an exact instance of a particular class

Attributes:
    obj (class object): object to evaluate
    a_class           : class to evaluate against

Return:
    bool True/False
"""


def is_same_class(obj, a_class):
    """
    determine of obj is an exact instance of type a_class
    """

    return type(obj) == a_class
