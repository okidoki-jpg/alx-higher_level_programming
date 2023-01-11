#!/usr/bin/pythin3
"""
Class Module Doc: Square

Attributes:
    Rectangle (class): base class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Doc: Defines Square class

    Methods:
        __init__ - initialize obj
        __str__ - return string rep of obj
        area - calculates area of obj
    """

    def __init__(self, size):
        """
        instantiation of the rectangle

        Attributes:
            size (int): dimension of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        custom string representation

        Return:
            formated string
        """

        return f"[Square] {self.__sizr} / {self.__size}"

    def area(self):
        """
        calculates area of the square

        Return: Square area
        """

        return self.__size ** 2
