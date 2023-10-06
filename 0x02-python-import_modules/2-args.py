#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argumets = sys.argv
    first_argument = argumets[0]
    remaining_arguments = argumets[1:]
    length_of_args = len(remaining_arguments)

    if length_of_args <= 0:
        print("0 arguments.")
    elif length_of_args == 1:
        print("{:d} argument:".format(length_of_args))
        print("{:d}: Hello".format(length_of_args))
    elif length_of_args > 1:
        print("{:d} arguments:".format(length_of_args))
        for i in remaining_arguments:
            print("{:d}: {:s}".format(remaining_arguments.index(i) + 1, i))
