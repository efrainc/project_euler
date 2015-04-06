#! /usr/bin/env python


def largest_prime(num):
    prime = 0
    n = 2
    while num > n:
        while num % n != 0:
            n += 1
            if n > prime:
                prime = n
        num = num / n
    return prime

if __name__ == '__main__':
    print largest_prime(600851475143)

