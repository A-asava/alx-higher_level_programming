#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a class"""

    def __init__(self, size=0):
        """Initialize a class square
        Args: size -  this is the size of the square
        Raises:
            TypeError: if size is not an interger type
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
