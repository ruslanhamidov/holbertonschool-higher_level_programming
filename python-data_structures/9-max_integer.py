#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = 0
    for i in my_list:
        if i < 0 and abs(i) > biggest:
            biggest = i
        if i > biggest:
            biggest = i
    return biggest
