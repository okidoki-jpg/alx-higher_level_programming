#!/usr/bin/python3
"""
Class Module Doc: Define rectangle class

Attributes:
    Base (class): base class
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Doc: Define rectangle class

    Attributes:
        width (int): Rectangle width
        height (int): Rectangle height
        x (int): Rectangle x offset
        y (int): Rectangle y offset
        id (int): Object id
        icon (str): icon used to display shape
    """

    icon = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Method Doc: Initialize Rectangle
        """

        self.validate_size("width", width)
        self.validate_size("height", height)
        self.validate_plot("x", x)
        self.validate_plot("y", y)

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        int: Width of instamce

        Return:
            Rectangle width
        """

        return self.__width

    @width.setter
    def width(self, val):
        """
        set/modify width of instance
        """

        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """
        int: Height of instamce

        Return:
            Rectangle height
        """

        return self.__height

    @height.setter
    def height(self, val):
        """
        set/modify width of instance
        """

        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """
        int: X value of instamce

        Return:
            Rectangle x value
        """

        return self.__x

    @x.setter
    def x(self, val):
        """
        set/modify x value of instance
        """

        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """
        int: y value of instamce

        Return:
            Rectangle width
        """

        return self.__y

    @y.setter
    def y(self, val):
        """
        set/modify y value of instance
        """

        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def validate_size(self, name, val):
        """
        Validate dimension value
        """

        if type(val) is not int:
            raise TypeError(f"{name} must be an integer")
        if val <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_plot(self, name, val):
        """
        Validate coordinate value
        """

        if type(val) is not int:
            raise TypeError(f"{name} must be an integer")
        if val < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """
        Calculate shape area

        Return:
            Rectangle area
        """

        return (self.__width * self.__height)

    def display(self):
        """
        display rectangle using string defined in Rectangle.icon
        """

        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("".join([Rectangle.icon] * self.__width))

    def __str__(self):
        """
        Return:
            Shape properties
        """
        plots = f"{self.x}/{self.y}"
        size = f"{self.width}/{self.height}"

        return f"[Rectangle] ({self.id}) {plots} - {size}"

    def update(self, *args, **kwargs):
        """
        update object attributes using args/kwargs
        """

        if args:
            attrs = list(self.__dict__.keys())[:len(args)]
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
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
