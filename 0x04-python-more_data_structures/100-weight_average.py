#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_sum = 0
    total_weight = 0

    for int_tuple in my_list:
        weight_sum += int_tuple[0] * int_tuple[1]
        total_weight += int_tuple[1]
    average = weight_sum / total_weight
    return average
