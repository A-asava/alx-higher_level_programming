#!/usr/bin/python3
"""This module defines a function check for subclass"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class ;
        otherwise False
    Args:
        obj: object
        a_class: class
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
