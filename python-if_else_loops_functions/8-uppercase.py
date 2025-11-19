#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 64 and ord(i) < 91:
            print("{}".format(i), end="")
        else:
            print("{}".format(chr(ord(i) - 32)), end="")
    print()
