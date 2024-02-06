#!/usr/bin/python3
"""This module defines a json"""
import json


def to_json_string(my_obj):
    """This function returns the json representation of an object
    string
    Args:
        my_obj: object string
    """

    return json.dumps(my_obj)
