#!/usr/bin/python3
"""This module defines a function that return True if an object
    is an instance of the class inherited from
"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of, or if the
        object is an instance of a class that inherited from,
        the specified class ; otherwise
    Args:
        obj: object
        a_class: class
    """

    if isinstance(obj, a_class):
        return True
    return False
