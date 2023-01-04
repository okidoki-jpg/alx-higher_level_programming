#!/usr/bin/python3

"""
A class defining a rectangle.
"""


class Rectangle:

    """
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):

        """
        Initialize class attributes.
        """

        self.height = height
        self.width = width

    @property
    def width(self):

        """
        int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, val):

        """
        Set/modify instance width.
        """

        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):

        """
        int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, val):

        """
        Set/modify instance height.
        """

        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):

        """
        Returns the area of the rectangle
        """

        return self.width * self.height

    def perimeter(self):

        """
        Returns the perimeter of the rectangle
        """

        if all([self.__width, self.__height]):
            return 2 * (self.width + self.height)
        return 0
