#!/usr/bin/python3
"""
Class Module Doc: BaseGeometry
"""


class BaseGeometry:
    """
    Class Doc: Defines BaseGeometry class

    Methods:
        area - raises exception
        integer_validator - validates value variable
    """

    def area(self):
        """
        raises an exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates that value is type int greater than 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
