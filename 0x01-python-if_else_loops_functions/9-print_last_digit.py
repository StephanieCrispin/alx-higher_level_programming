#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        last_digit = ((number * -1) % 10)
    else:
        last_digit = number % 10
    if last_digit > 5:
        print("{:d}".format(last_digit), end="")
    elif last_digit == 0:
        print("{:d}".format(last_digit), end="")
    elif last_digit < 6 and not 0:
        print("{:d}".format(last_digit), end="")
    return last_digit


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
