#!/usr/bin/python3

"""
Print a formated string: My name is <first name> <last name>

Attributes:
    first_name (string): string var holding first name
    last_name (string) : string var holding last name
"""


def say_my_name(first_name, last_name=""):

    """
    Validate that first/last _name is a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    """
    print formated string
    """
    print(f"My name is {first_name} {last_name}")
