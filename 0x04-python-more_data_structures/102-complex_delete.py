#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_keys = list(a_dictionary.keys())
    for i in dict_keys:
        if value == a_dictionary.get(i):
            del a_dictionary[i]
    return a_dictionary
