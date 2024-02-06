#!/usr/bin/python3
"""This mode represent a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representyss a class rectangle"""

    def __init__(self, width, height):
        """Initializing a class rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """returns print() and str() representation of a rectangle"""

        return ("[{}] {}/{}".format(self.__class__.__name__,
                self.__width, self.__height))
