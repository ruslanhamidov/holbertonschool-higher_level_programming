#!/usr/bin/python3
def no_c(my_string):
    l = list(my_string)
    for i in range(len(l)):
        if i >= len(l):
            break
        if l[i] == 'c' or l[i] == 'C':
            del l[i]

    return "".join(l)
