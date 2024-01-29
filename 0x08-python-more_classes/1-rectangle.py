#!/usr/bin/python3

"""Defining class rectangle"""


class Rectangle:
    """Representing the class"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args:
            width: width size of the rectangle
            height: height size of the square
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width size"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
