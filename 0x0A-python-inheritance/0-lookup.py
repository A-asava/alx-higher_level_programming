#!/usr/bin/python3
"""This module defines a function that return a list of
    available attributes and methods in an object
"""


def lookup(obj):
    """Return a list of attributes and methods in an object
    Args:
        obj: object to look
    """

    return dir(obj)
