#! /usr/bin/env python


def sum_square_difference():
    """Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum"""

    sum_squares = 0
    sum_numbers = 0
    for x in xrange(1, 101):
        sum_squares += x ** 2
        sum_numbers += x

    difference = sum_numbers ** 2 - sum_squares

    return difference


if __name__ == "__main__":
    print sum_square_difference()
