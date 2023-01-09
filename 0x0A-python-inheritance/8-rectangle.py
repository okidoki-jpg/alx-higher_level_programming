#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Class Module Doc: Rectangle

Attributes:
    BaseGeometry (class object): base class
"""


class Rectangle(BaseGeometry):
    """
    Class Doc:Defines Rectangle class
    """

    def __init__(self, width, height):
        """
        instantiate rectangle

        Attributes:
            width (int): rectangke width
            height (int): rectangke height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
