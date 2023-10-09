#!/usr/bin/python3
def max_integer(my_list=[]):
    count = 0

    for i in my_list:
        if int(i) > count:
            count = int(i)
        print(i)

    return count
