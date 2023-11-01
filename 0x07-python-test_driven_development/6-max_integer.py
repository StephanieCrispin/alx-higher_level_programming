#!/usr/bin/python3
"""Find max integer in a list"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integer
    """
    if len(list) == 0:
        return None
    res = list[0]
    x = 1

    while x < len(list):
        if list[x] > res:
            res = list[x]
        x = x + 1
    return res
