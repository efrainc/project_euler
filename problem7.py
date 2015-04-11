#! /usr/bin/env python


def find_prime(num):
    prime = 0
    n = 2
    while num > n:
        if num % n != 0:
            n += 1
            if n > prime:
                prime = n
        else:
            return None
    if prime == num:
        # print "the number is prime"
        return prime
    return None


def find_xprime(number):
    primes = [1,2,3,5,7,11,13]
    test_number = 14
    while len(primes) < number+1:
        result = find_prime(test_number)
        if result > 0:
            primes.append(result)
        test_number += 1
    return primes[-1]


if __name__ == '__main__':
    # print find_prime(44)
    print find_xprime(10001)
