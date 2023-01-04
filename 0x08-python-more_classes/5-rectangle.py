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

        self._Rectangle__height = height
        self._Rectangle__width = width

    @property
    def width(self):

        """
        int: The width of the rectangle.
        """

        return self._Rectangle__width

    @width.setter
    def width(self, val):

        """
        Set/modify instance width.
        """

        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = val

    @property
    def height(self):

        """
        int: The height of the rectangle.
        """

        return self._Rectangle__height

    @height.setter
    def height(self, val):

        """
        Set/modify instance height.
        """

        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = val

    def area(self):

        """
        Returns the area of the rectangle
        """

        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):

        """
        Returns the perimeter of the rectangle
        """

        if any([self._Rectangle__width, self._Rectangle__height]) == 0:
            return 0
        return 2 * (self._Rectangle__width + self._Rectangle__height)

    def __str__(self):

        """
        Returns a string representation of the rectangle using the character #.
        """

        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):

        """
        Returns string representation of instanciation call with
        self attributes.
        """

        width = self._Rectangle__width
        height = self._Rectangle__height
        o = f'{self.__class__.__name__}({width}, {height})'
        return o

    def __del__(self):

        """
        Prints a message when the object is deleted.
        """

        print('Bye rectangle...')
