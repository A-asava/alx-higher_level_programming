#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent a class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class
        Args:
            size: size of square
            position: position of the square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of a square"""

        return (self.__size ** 2)

    def my_print(self):
        """print the square"""

        if self.__size == 0:
            print("")

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
