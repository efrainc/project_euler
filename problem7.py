#! /usr/bin/env python


import math


def check_if_prime(num):
    """Determine if input is a prime number"""

    for item in xrange(2, int(math.sqrt(num)+1)):
        if num % item == 0:
            return None
    return num


def find_xprime(number):
    """Find the prime number that is the selected input in
    sequence starting at 1"""

    # List of first primes generated for understanding
    primes = [1, 2, 3, 5, 7, 11, 13]
    test_number = 14
    while len(primes) < number+1:
        result = check_if_prime(test_number)
        if result > 0:
            primes.append(result)
        test_number += 1
    return primes[-1]


if __name__ == '__main__':
    print find_xprime(10001)
