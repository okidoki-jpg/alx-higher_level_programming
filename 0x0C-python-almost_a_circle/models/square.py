#!/usr/bin/python3
"""
Class Module Doc: Define a Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Doc: Define a Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Method Doc: Initialize Square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return:
            Shape properties
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """
        int: size of instamce

        Return:
            Square dimension
        """

        return self.height

    @size.setter
    def size(self, val):
        """
        set/modify dimension of instance
        """

        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        update object attributes using args/kwargs
        """

        attrs = list(Square.__init__.__code__.co_varnames)[1:]
        attrs.insert(0, attrs.pop())

        if args:
            for k, v in zip(attrs, args):
                setattr(self, k, v)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Return:
            Dictionary representation of object
        """

        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
