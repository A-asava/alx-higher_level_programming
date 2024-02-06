#!/usr/bin/python3
"""This module defines a function that decode"""
import json


def load_from_json_file(filename):
    """This function creates an object from json file"""

    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
