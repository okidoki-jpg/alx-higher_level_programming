#!/usr/bin/python3

"""
Module Doc:

Return:
    simple data structure dictionary dsscriptiom
"""


def class_to_json(obj):
    """
    Function Doc: Return dictionary for serializatiom
    """

    return obj.__dict__
