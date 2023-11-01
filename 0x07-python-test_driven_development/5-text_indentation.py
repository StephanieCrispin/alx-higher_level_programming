#!/usr/bin/python3
"""Defines a function that indents a text"""


def text_indentation(text):
    """Print text with two new lines after '.', '?' or ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    num = 0
    while num < len(text) and text[num] == ' ':
        num += 1

    while num < len(text):
        print(text[num], end="")
        if text[num] == "\n" or text[num] in ".?:":
            if text[num] in ".?:":
                print("\n")
            num += 1
            while num < len(text) and text[num] == ' ':
                num += 1
            continue
        num += 1
