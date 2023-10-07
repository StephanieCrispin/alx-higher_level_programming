#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arguments = sys.argv[1:]
    if len(arguments) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif len(arguments) == 3:
        a = int(arguments[0])
        b = int(arguments[2])
        c = arguments[1]
        if c == "-":
            print("{:d} {:s} {:d} = {:d}".format(a, c, b, sub(a, b)))
        elif c == "+":
            print("{:d} {:s} {:d} = {:d}".format(a, c, b, add(a, b)))
        elif c == "/":
            print("{:d} {:s} {:d} = {:d}".format(a, c, b, div(a, b)))
        elif c == "*":
            print("{:d} {:s} {:d} = {:d}".format(a, c, b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
