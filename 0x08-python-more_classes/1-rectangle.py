#!/usr/bin/python3

"""Defining class rectangle"""


class Rectangle:
    """Representing  class"""

    def __init__(self, width=0, height=0):
        """Initiating the rectangle class
        Args:
            width: width of rectangle
            height: height  of th square
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Fetches the width size"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an type int")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Fetches the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be type int")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
