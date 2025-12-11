#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in range(x):
            print(my_list[i], end="")
            num += 1
        print()
        return num
    except KeyError:
        print("Index out of range")
