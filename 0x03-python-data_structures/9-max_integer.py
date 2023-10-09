#!/usr/bin/python3
def max_integer(my_list=[]):

    if not my_list:
        return None
    if isinstance(my_list, list):
        count = 0
        for i in my_list:
            if int(i) > count:
                count = int(i)
        return count
