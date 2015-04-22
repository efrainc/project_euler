#! /usr/bin/env python


def fibonacci():
    """Find the fibonacci term with 1000 or more digits"""

    n1 = 1
    n2 = 2
    nth = 0
    # given that the first number with a 1000 digit is 10 ** 999
    thousands = 10 ** 999
    count = 4
    while True:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        if nth > thousands:
            return count, len(str(nth)), n1
        count += 1

if __name__ == '__main__':
    print fibonacci()