#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = set(my_list)
    i = 0
    for k in new_set:
        i += k

    return (i)


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
