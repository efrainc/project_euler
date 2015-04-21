#! /usr/bin/python


import time


def number_routs(cube_size=20):
    """Find routes using mathimatical summation of sum of paths
    for each node in a matrix structure"""

    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]


def measureTime(a):

    start = time.clock()
    print a()
    elapsed = time.clock()
    final = elapsed - start

    print "Time spent in (%s) is: " % (a.func_name) + str(final)

if __name__ == '__main__':
    measureTime(number_routs)
