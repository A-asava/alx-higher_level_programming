#!/usr/bin/python3
"""This module defines a class"""


class BaseGeometry:
    """Representing a class BaseGeometry"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value of an integer
        Args:
            name: Argument 1
            Value: argument 2
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
