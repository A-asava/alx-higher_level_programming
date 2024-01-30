#!/usr/bin/python3
"""Define a class"""


class LockedClass:
    """This class prevents the user from dynamically
    creating a new instance atrributes, except when new instance
    attribute
    """

    __slot__ = ["first_name"]
