#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """This function divides all the element in matrix by div
    Args:
        matrix: represents a list of elements in matrix form
        div: the divisor
    """

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        for element in row:
            if not isinstance(element, int) and not isinstance(element, float):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        result_row = list(map(lambda x: round(x / div, 2), row))
        result.append(result_row)

    return result
