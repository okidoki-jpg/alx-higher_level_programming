#!/usr/bin/python3

class Square:
    """A class defining a Square"""

    def __init__(self, size=0):
        """Initialization of class properties
    
            Args:
                size (:obj:`int`, optional): size of square. used to
                init private size attr.

            Raises:
                TyoeError: if size variable is not int
                ValueError: if size variable is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
