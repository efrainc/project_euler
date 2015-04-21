#! /usr/bin/env python


def power_digit_sum():
    """Find the sum of the digits of the number 2 ** 1000"""

    number = 2 ** 1000
    stringify = str(number)
    total = 0
    for i in stringify:
        total += int(i)
    return total


if __name__ == '__main__':
    print power_digit_sum()
