#!/usr/bin/python3
"""Prints all integers of a list"""
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        [print("{:d}".format(item)) for item in my_list]
