#!/usr/bin/python3
"""This module defines a function"""


def read_file(filename=""):
    """Initiatializing a function read_file that reads a text file
        and print it
    Args:
        filename: file to be read
    """

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
