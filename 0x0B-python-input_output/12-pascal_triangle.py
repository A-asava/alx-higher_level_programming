#!/usr/bin/python3
"""This module defines a function"""


def pascal_triangle(n):
    """Returns a list of lists of intergers representing
        the pascal triangle
    """

    triangle = []
    if n <= 0:
        triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            for x in range(len(prev_row) - 1):
                row.append(prev_row[x] + prev_row[x + 1])
            row.append(1)
        triangle.append(row)
    return triangle
