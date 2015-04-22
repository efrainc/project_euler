#! /usr/bin/env python


import math


def factorial_digit_sum():
    """Find the sum of the digits in for the factorial of 100"""

    num = math.factorial(100)
    stringify = str(num)
    total = 0
    for i in stringify:
        total += int(i)

    return total

if __name__ == '__main__':
    print factorial_digit_sum()
