#! /usr/bin/env python

import time


def factorial(num):
    """Find list of unique factors for a number"""

    l = []
    for i in xrange(1, (int(num**0.5) + 1), 1):
        if num % i == 0:
            l += [i] + [num/i]
    return len(set(l))


def factorial2(num):
    """Testing with appened method for time of execution"""

    l = []
    for i in xrange(1, (int(num**0.5) + 1), 1):
        if num % i == 0:
            l.append(i)
            l.append(num/i)
    return len(set(l))


def factorial3(num):
    """Testing using concatination and reduce function"""

    return set(reduce(list.__add__,
               ([i, num//i] for i in xrange(1, int(num**0.5) + 1) if num % i == 0)))


def triangle_factor():
    """Find the first number with greater than 500 factors"""

    sum = 0
    count = 1
    while True:
        # for i in xrange(1, 99999999999999, 1):
        sum += count
        count += 1
        if factorial(sum) > 500:
            return sum


def triangle_factor2():
    """Find the first number with greater than 500 factors
    using append"""

    sum = 0
    count = 1
    while True:
        # for i in xrange(1, 99999999999999, 1):
        sum += count
        count += 1
        if factorial2(sum) > 500:
            return sum


def triangle_factor3():
    """Find the first number with greater than 500 factors
    using xrange and reduce function"""

    sum = 0
    for i in xrange(1, 99999999999999, 1):
        sum += i
        if len(factorial3(sum)) > 500:
            return sum


def measureTime(a):

    start = time.clock()
    a()
    elapsed = time.clock()
    final = elapsed - start

    print "Time spent in (function name) is: " + str(final)

if __name__ == '__main__':
    measureTime(triangle_factor)
    measureTime(triangle_factor2)
    measureTime(triangle_factor3)
