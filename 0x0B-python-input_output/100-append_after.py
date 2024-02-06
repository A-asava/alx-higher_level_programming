#!/usr/bin/python3
"""This module defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """This function inserts a line of text to a file
        after each line containing a specific string
    """

    text = ""
    with open(filename, "r") as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
