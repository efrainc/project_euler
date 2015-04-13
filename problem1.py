#! /usr/bin/env python


def problem1():
    """Prints the sum of numbers divisible by 3
    or 5 from numbers 1 - 1000"""

    total = 0
    for number in xrange(1000):
        if number % 3 == 0 or number % 5 == 0:
            total += number
    return total


if __name__ == '__main__':
    print problem1()
