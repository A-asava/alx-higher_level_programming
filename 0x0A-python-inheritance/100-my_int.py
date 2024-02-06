#!/usr/bin/python3
"""This module defines a class that inherits from superclass"""


class MyInt(int):
    """Represents a class MyInt that inherits from int"""

    def __eq__(self, val):
        """this funtion overides value with !="""

        return self.real != val

    def __ne__(self, val):
        """Overides val"""

        return self.real == val
