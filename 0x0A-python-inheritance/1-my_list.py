#!/usr/bin/python3
""" A class """


class MyList(list):

    """ A class that inherits from list"""

    def print_sorted(self):
        """ A method that prints out a sorted list"""
        print(sorted(self))
