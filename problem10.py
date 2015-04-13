#! /usr/bin/env python

from problem7 import check_if_prime


def sum_of_primes(number):
    """Find the prime numbers starting from two till the number is
    less than or equal to the input"""

    # List of first primes generated for understanding
    primes = [2, 3, 5, 7, 11, 13]
    test_number = 14
    while test_number <= number:
        result = check_if_prime(test_number)
        if result > 0:
            primes.append(result)
        test_number += 1
    return sum(primes)


if __name__ == '__main__':
    print sum_of_primes(2000000)

