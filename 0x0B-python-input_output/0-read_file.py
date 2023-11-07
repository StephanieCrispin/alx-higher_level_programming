#!/usr/bin/python3
def read_file(filename=""):
    """ Reads from a text file """
    with open(filename, encoding="utf-8") as f:
        read = f.read()
        print(read, end="")
