#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if not length:
        return (0, None)
    char = sentence[0]
    return (length, char)
