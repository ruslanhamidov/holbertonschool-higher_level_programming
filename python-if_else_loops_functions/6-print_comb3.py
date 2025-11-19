#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == j:
            continue
        if j < i:
            continue
        if i == 8:
            print("{}{}".format(i, j))
            break
        print("{}{}".format(i, j), end=", ")
