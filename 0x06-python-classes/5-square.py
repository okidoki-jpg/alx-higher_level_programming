#!/usr/bin/python3
"""Creating a square class"""


class Square:
    """A clasd defining a square"""

    def __init__(self, size=0):
        """Initialization of class properties

            Args:
                size (:obj:`int`, optional): size of square. used to
                init private size attr.
        """

        self.size = size

    @property
    def size(self):
        """
        Returns:
            int: size value of the square
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
            Args:
                value: variable to set Square size

            Raises:
                TyoeError: if size variable is not int
                ValueError: if size variable is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns:
            int: area of the square
        """

        return (self.__size * self.__size)

    def my_print(self):
        """Print Square instance"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
