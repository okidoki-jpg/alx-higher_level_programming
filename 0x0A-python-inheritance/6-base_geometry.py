#!/usr/bin/python3
"""
Class Module Doc: BaseGeometry
raise exception for undeclared area
"""


class BaseGeometry:
    """
    Class doc: Defines BaseGeometry class

    Methods:
        area - raises exception
    """

    def area(self):
        """
        raises an exception
        """

        raise Exception("area() is not implemented")
