#!/usr/bin/python3
"""
Class Module Doc: Square

Attributes:
    Rectangle (class): base class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Doc: Defines Square class
    """

    def __init__(self, size):
        """
        instantiate square

        Attributes:
            size (int): dimension of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
