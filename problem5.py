#! /usr/bin/env python


def smallest_multiple():
    """Find the smallest number for which the numbers
    1 through 20 can divided by and the result has
    reminder"""

    number = 2000
    while True:
        if check_remainder(number) == 'Yes':
            return number
        number += 20


def check_remainder(num):
    """Check that all numbers in range can evenly
    divided the number"""

    for x in xrange(1,21):
        if num % x == 0:
            pass
        else:
            return 'Nope'
    return 'Yes'


if __name__ == '__main__':
    print smallest_multiple()

