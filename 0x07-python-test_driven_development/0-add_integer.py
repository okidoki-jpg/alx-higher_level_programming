#!/usr/bin/python3

"""
Addition function

Cast two values to type int and return sum of the two int values
"""


def add_integer(a, b=98):

    """
    Atttibutes:
        a (any tyoe): Value to be cast to int
        b (any tyoe): Value to be cast to int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
