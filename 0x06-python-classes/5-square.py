#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent a class"""

    def __init__(self, size=0):
        """Initialize a square
        Args: size - size of the square
        """

        self.size = size

    @property
    def size(self):
        """Retrieve a size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """ that prints in stdout the square with the character #"""

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
