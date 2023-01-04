#!/usr/bin/python3

"""
A class defining a rectangle.
"""


class Rectangle:

    """
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of rectangle instances.
        print_symbol (any type): The symbol used for the string
            representation of the rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        """
        Initialize class attributes.
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

        return self.__width * self.__height

    def perimeter(self):

        """
        Returns the perimeter of the rectangle
        """

        if all([self.__width, self.__height]):
            return 2 * (self.__width + self.__height)
        return 0

    def __str__(self):

        """
        Returns a string representation of the rectangle using the character #.
        """

        if all([self.width, self.height]):
            return '\n'.join([str(self.print_symbol)*self.width] * self.height)
        return ""

    def __repr__(self):

        """
        Returns string representation of instanciation call with
        self attributes.
        """

        width = self.__width
        height = self.__height
        o = f'{self.__class__.__name__}({width}, {height})'
        return o

    def __del__(self):

        """
        Prints a message when the object is deleted.
        """

        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):

        """
        Returns a new Rectangle instance with
        width == height == size
        """

        return cls(size, size)
