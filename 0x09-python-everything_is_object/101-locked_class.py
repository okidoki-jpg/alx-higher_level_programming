#!/usr/bin/python3

"""
Limited class that only allows creation of "first_name" variable
"""


class LockedClass:

    """
    Allowed variables
    """
    __slots__ = ["first_name"]
