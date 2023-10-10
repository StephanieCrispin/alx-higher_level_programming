#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    char = sentence[0]
    if not length:
        sentence[0] = None
    newtupple = (length, char)
    return (newtupple)


sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
