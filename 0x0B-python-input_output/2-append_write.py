#!/usr/bin/python3
"""This module defines a function that append a file"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file
        and return the number of characters printed
    Args:
        filename: file to append text to
        text: text to append
    """

    with open(filename, "a", encoding="utf-8") as file:
        char_added = file.write(text)
        return char_added
