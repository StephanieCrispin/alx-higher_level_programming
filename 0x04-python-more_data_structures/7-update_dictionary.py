#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_dict = dict()
    new_dict = a_dictionary
    new_dict.update({key: value})
    return (new_dict)
