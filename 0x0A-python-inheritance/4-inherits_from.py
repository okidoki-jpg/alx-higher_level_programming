#!/usr/bin/python3
"""
Module Doc: inherits_from
determine if obj is a subclass

Attributes:
    obj (class object): object to evaluate
    a_class           : class to evaluate against

Return:
    bool True/False
"""


def inherits_from(obj, a_class):
    """
    determine if obj is a subclass
    """

    return isinstance(obj, a_class) and type(obj) != a_class
