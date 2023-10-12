#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    new_dict = a_dictionary
    result_dict = dict()
    for key, value in new_dict.items():
        result_dict.update({key: value * 2})
    return (result_dict)
