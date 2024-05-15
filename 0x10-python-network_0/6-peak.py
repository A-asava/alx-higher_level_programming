#!/usr/bin/python3
"""
    function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """_summary_

    Args:
        list_of_integers (int): list of integers to find the peak of
    Returns: The peak of list_of_integers or none if list is empty
    """

    size = len(list_of_integers)
    low = 0
    high = size - 1

    if size == 0:
        return None

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
