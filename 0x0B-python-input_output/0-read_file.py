#!/usr/bin/python3
"""Defines a function that reads from a text file"""


def read_file(filename=""):
    """Function that reads from my text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
