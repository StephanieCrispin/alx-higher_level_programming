#!/usr/bin/python3
"""This file defines a function that reads from a text file"""


def read_file(filename=""):
    """ Reads from a text file """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read, end="")
