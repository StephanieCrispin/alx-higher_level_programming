#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = dict()

    new_dict = a_dictionary
    if new_dict.get(key) == None:
        return (new_dict)
    else:
        new_dict.pop(key)
        return (new_dict)
