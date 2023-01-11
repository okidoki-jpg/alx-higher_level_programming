#!/usr/bin/python3
"""
Class Module Doc:  Rectangle

Attributes:
    BaseGeometry (class object): base class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Doc: Defines Rectangle class

    Methods:
        __init__ - initialize obj
        __str__ - return string rep of obj
        area - calculates area of obj
    """

    def __init__(self, width, height):
        """
        instantiate rectangle

        Attributes:
            width (int): rectangle width
            height (int): rectangle height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        custom str method for print the rectangle

        Return:
            formated string
        """

        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        calculates area of the retangle

        Return: Rectangke area
        """

        return self.__width * self.__height
