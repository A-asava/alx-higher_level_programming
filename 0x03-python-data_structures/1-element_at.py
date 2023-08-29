#!/usr/bin/python3
def element_at(my_list, idx):
    count = len(my_list) - 1
    if idx < 0 or idx > count:
        return None
    return (my_list[idx])
