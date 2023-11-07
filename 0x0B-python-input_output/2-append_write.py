#!/usr/bin/python3

def append_write(filename="", text=""):
    """An object that appends a string to a text file"""
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
