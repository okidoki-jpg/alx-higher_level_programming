#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.__position = position

    @property
    def size(self):

        return (self.__size)

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):

        return (self.__size * self.__size)

    @property
    def position(self):

        return (self.__position)

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or\
        not all(isinstance(idx, int) for idx in value) or\
        not all(idx >= 0 for idx in value) or len(value) != 2:
            raise TypeError("position must be a tuple of two integers")
        
        self.__position = value


    def my_print(self):

        if self.__size == 0:
            print()
            return

        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print()
