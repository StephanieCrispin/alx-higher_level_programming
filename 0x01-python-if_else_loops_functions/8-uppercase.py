#!/usr/bin/python3
def uppercase(str):
    for k in str:
        i = (ord(k))
        i -= 32
        print(chr(i), end="")
    print("\n")
