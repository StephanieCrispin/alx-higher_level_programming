#!/usr/bin/python3
if __name__ == "__main__":
    """Program that adds all arguments to a single value"""
    import sys
    arguments = sys.argv
    remaining_arguments = arguments[1:]
    result = 0
    for i in remaining_arguments:
        result += int(i)
    print("{}".format(result))
