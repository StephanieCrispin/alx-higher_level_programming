#!/usr/bin/python3
for i in range(0,100):
    if i < 10:
       i = ("{:02}, ".format(i))
    elif i != 99:
       i = ("{:d}, ".format(i))
    elif i == 99:
       i = ("{:d}\n").format(i)
    print(i, end=" ")
    