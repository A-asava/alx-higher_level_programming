#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_dict = sorted(a_dictionary.keys())
    for key in ord_dict:
        print("{}: {}".format(key, a_dictionary.get(key)))
