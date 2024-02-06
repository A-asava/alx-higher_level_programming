#!/usr/bin/python3
"""This module defines a class"""


class Student:
    """Representing a class"""

    def __init__(self, first_name, last_name, age):
        """Initailizing the class student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function retrieves a dictionary representation
        of a student
        """

        return self.__dict__
