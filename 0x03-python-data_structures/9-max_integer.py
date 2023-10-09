#!/usr/bin/python3
def max_integer(my_list=[]):

    if my_list == []:
        return (None)

    # count = 0
    # for i in my_list[:len(my_list)]:
    #     if int(i) > count:
    #         count = int(i)
    # return count
    max_value = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > max_value:
            max_value = my_list[x]
    return (max_value)
