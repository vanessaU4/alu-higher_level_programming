#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max_number = my_list[0]
    for number in my_list:
        if number > max_number:
            max_number = number
    return max_number
    