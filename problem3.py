#! /usr/bin/env python


def largest_prime(num):
    """Find the largest prime for a input number"""

    prime = 0
    divisor = 2
    while num > divisor:
        while num % divisor != 0:
            divisor += 1
            if divisor > prime:
                prime = divisor
        num = num / divisor
    return prime


if __name__ == '__main__':
    print largest_prime(600851475143)
