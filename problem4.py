#! /usr/bin/env python


def probl4():
    """Find the largest palindrome made by
    the products of x and y. Values between 101
    and 1000"""

    largest_palindrome = 0
    for i in xrange(101, 1000):
        for j in xrange(101, 1000):
            output = i * j
            if str(output) == str(output)[::-1] and \
                    output > largest_palindrome:
                largest_palindrome = output
    return largest_palindrome


if __name__ == '__main__':
    print probl4()

