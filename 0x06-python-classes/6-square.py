#!/usr/bin/python3
"""Creating a square class"""


class Square:
    """A clasd defining a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of class properties

            Args:
                size (:obj:`int`, optional): size of square. used to
                init private size attr.

                position (:obj:`tuple`, optional): coordinates of
                square instance
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves instance position

            Returns:
                tuple: position of the square
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets position of square instance

            Raises:
                TypeError: If data is incompatible
        """

        if not isinstance(value, tuple) or
        not all(isinstance(idx, int) for idx in value) or
        not all(idx >= 0 for idx in value) or len(value) != 2:
            raise TypeError("position must be a tuple of two integers")

        self.__position = value

    def my_print(self):
        """Print Square instance"""

        if self.__size == 0:
            print()
            return

        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print()
