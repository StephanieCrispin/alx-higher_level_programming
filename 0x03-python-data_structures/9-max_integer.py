#!/usr/bin/python3
def max_integer(my_list=[]):

    if my_list == []:
        return None

    count = 0
    for i in my_list[:len(my_list)]:
        if int(i) > count:
            count = int(i)
    return count
