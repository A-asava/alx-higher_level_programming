#!/usr/bin/python3
"""This module defines a class that inherits from another superclass"""


class MyList(list):
    """A class that inherits from a list"""

    def print_sorted(self):
        """This method prints the list in a sorted manner"""

        print(sorted(self))
