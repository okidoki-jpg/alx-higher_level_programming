

from base import Base

class Base:
    __nb_objects = 0

    def __init__(self, id=None):

        self.id = id

        if not id:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
    
class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, val):

        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, val):

        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):

        return self.__x

    @x.setter
    def x(self, val):

        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):

        return self.__y

    @y.setter
    def y(self, val):

        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val
