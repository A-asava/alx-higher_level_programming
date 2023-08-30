#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent a class"""

    def __init__(self, size=0):
        """Initialize a square class
        Args: size - represents size of a square
        """

        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""

        return (self.__size ** 2)
