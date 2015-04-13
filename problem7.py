#! /usr/bin/env python


def check_if_prime(num):
    """Determine if input is a prime number"""

    denominator = 2
    while num > denominator:
        if num % denominator != 0:
            denominator += 1
            found_prime = denominator
        else:
            return None
    if found_prime == num:
        return found_prime
    return None


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
