#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if not length:
        return (0, None)
    char = sentence[0]
    return (length, char)


sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
