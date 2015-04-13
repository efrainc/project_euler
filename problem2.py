#! /usr/bin/env python


def fibtest():
    """Calculates the sum of even fibonacci
    numbers between 0 and 4000000"""

    i = 0
    first = 1
    second = 2
    total = 2
    while i < 4000000:
        i = first + second
        first = second
        second = i
        if i % 2 == 0:
            total += i
    return total


if __name__ == '__main__':
    print fibtest()
