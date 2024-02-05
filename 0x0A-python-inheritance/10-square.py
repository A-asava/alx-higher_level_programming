#!/usr/bin/python3
"""This module defines a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a class square"""

    def __init__(self, size):
        """Initializing a class"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
