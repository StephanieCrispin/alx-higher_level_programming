#!/usr/bin/python3
for k in range(0, 9):
    for w in range(0, 10):
        if k > w:
            continue
        if w == 9 and k == 8:
            print("{:d}{:d}".format(k, w))
            break
        else:
            print("{:d}{:d}".format(k, w), end=", ")
