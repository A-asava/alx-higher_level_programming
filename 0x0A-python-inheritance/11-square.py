#!/usr/bin/python3
"""This module defines a subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a class square"""

    def __init__(self, size):
        """Initialize  the class square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
