#!/usr/bin/python3

"""Defining class rectangle"""


class Rectangle:
    """Representing the class rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing class rectangle
        Args:
            width: width size of the rectangle
            height: height size of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieves height"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Rteurns the area of the rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2*(self.__width + self.__height))
