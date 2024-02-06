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
                all(isinstance(key, str) for key in attrs):
            attr_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    attr_dict[attr] = getattr(self, key)
            return attr_dict

        return self.__dict__

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""

        for key, value in json.items():
            setattr(self, key, value)
