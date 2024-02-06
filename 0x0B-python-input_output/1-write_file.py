#!/usr/bin/python3
"""This module defines a function Write_file"""


def write_file(filename="", text=""):
    """The function writes to a text file and returns the number
        of characters printed
    Args:
        filename: file to write text to
        text: text to write in a file
    """

    with open(filename, "w", encoding="utf-8") as file:
        num_characters = file.write(text)
        return num_characters
