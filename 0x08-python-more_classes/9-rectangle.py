#!/usr/bin/python3

"""Defining a class"""


class Rectangle:
    """Representing the class rectangle
    Attribute:
        number_of_instances: represent the number of rectangle instances
        print_symbol: represent symbols used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the classs
        Args:
            width: width size of the rectangle
            height: height size of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width"""

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
        """Retrieves the height"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the triangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2*(self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area
        Args:
            rect_1: rectangle 1 to compare
            rect_2: rectangle 2 to compare
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Return  the printable representation of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        new_rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                new_rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                new_rect.append("\n")

        return ("".join(new_rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""

        return ("Rectangle({}, {}".format(self.__width, self.__height))

    def __del__(self):
        """Prints a message for every deletion"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
