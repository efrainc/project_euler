#! /usr/bin/env python

import time


def problem14():
    """Longest Collatz Sequence - Brute Force Method"""

    maximum = (0, 0)
    for a in xrange(2, 1000000):
        count = 0
        number = a
        while a != 1:
            if a % 2 == 0:
                a = a/2
            else:
                a = 3*a + 1
            count += 1
        if count > maximum[1]:
            maximum = (number, count)

    return maximum


"""
But Brute Foce is Ugly (speaking pythonincally) and wastes time!!!

Ideas for improvment:
Every time we calcualte a number 'a' value we should check against a
dictionary containings numbers and related steps to get to number 1. Basically
stop itteratting if we get a number we should have seen before.
"""


def problem14_version2():
    """Longest Collatz Sequence - Dictionary  Method"""

    maximum = (0, 0)
    holder = {}
    for a in xrange(2, 1000000):
        count = 0
        number = a
        while a != 1:
            try:
                holder[a]
                count += holder[a]
                break
            except KeyError:
                if a % 2 == 0:
                    a = a/2
                else:
                    a = 3*a + 1
                count += 1
        if count > maximum[1]:
            maximum = (number, count)
        holder[number] = count

    return maximum

"""
Results: Using the new methods reduces time from 20 seconds to 5 seconds.
Unfortunately, because we are creating a dictionary we are eating up a lot of
space. Also, using the Try and except to catch the error is not ideal - this
could be solved by initializing the dictionary with all zeros. But that would
take additional set up time.
"""


def measureTime(a):

    start = time.clock()
    a()
    elapsed = time.clock()
    final = elapsed - start

    print "Time spent in (%s) is: " % (a.func_name) + str(final)


if __name__ == '__main__':
    measureTime(problem14)
    measureTime(problem14_version2)

