#!/usr/bin/python3

""" A class """


def inherits_from(obj, a_class):
    """ Checks if an object's type is a subclass of a_class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
