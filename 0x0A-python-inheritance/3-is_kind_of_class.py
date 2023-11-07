#!/usr/bin/python3

""" A class """


def is_kind_of_class(obj, a_class):
    """ Checks if an object is a class type"""
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
