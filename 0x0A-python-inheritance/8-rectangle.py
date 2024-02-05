#!/usr/bin/python3
"""This module defines a class that inherits form superclass"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reperesents a class rectangle"""

    def __init__(self, width, height):
        """Initializeing a class
        Args:
            width: represents the width of the rectangle
            height: height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
