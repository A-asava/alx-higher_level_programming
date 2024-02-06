#!/usr/bin/python3
"""This module defines a class"""


class Student:
    """Representing a class"""

    def __init__(self, first_name, last_name, age):
        """Initializing a class student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of student"""

        if isinstance(attrs, list) and \
                all(isinstance(attr, str) for attr in attrs):
            attr_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attr_dict[attr] = getattr(self, attr)
            return attr_dict

        return self.__dict__
