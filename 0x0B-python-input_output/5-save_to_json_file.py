#!/usr/bin/python3
"""This modules define a function"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text using json representation"""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
