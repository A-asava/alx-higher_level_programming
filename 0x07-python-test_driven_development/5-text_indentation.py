#!/usr/bin/python3
"""Defining a function"""


def text_indentation(text):
    """Function that prints a text with 2 newlines after each
    this characters: .? and :
    Args:
        text: text to print
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1

        if flag == 1:
            if char in ('?', '.', ':'):
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
