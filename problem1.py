#! /usr/bin/env python


def problem1():
    total = 0
    for i in xrange(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
            print i
    return total


if __name__ == '__main__':
    print problem1()
