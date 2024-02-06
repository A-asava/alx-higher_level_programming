#!/usr/bin/python3
"""This module defines a function that return True if the object
    is exactly an instance of the specified class otherwise false
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified
    class
    Args:
        obj: Object to check
        a_class: class
    """

    if type(obj) == a_class:
        return True
    return False
