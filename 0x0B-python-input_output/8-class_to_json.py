#!/usr/bin/python3
"""Function module"""


def class_to_json(obj):
    """Returns the dictionary description with simple
        data structures
    """

    return obj.__dict__
