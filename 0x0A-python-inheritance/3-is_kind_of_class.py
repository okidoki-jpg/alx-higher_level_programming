#!/usr/bin/python3
"""
Module doc: is_kind_of_class
determine if obj is exact/inherited instance of a claas

Attributes:
    obj (class object): object to evaluate
    a_class           : class to evaluate against

Return:
    bool True/False
"""


def is_kind_of_class(obj, a_class):
    """
    determine if obj is exact/inherited instance of a claas
    """

    return isinstance(obj, a_class)
