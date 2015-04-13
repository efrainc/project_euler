#! /usr/bin/env python


def largest_prime(num):
    """Find the largest prime for a input number"""

    if num == 0:
        return 0

    prime = 1
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
