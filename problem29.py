#! /usr/bin/env python


def find_powers():
    """Calculates the result of unique power
    combinations for x^y in range 2-101 for
    both x and y"""

    final = []
    for x in xrange(2, 101):
        for y in xrange(2, 101):
            final.append(x**y)
    return len(set(final))


if __name__ == '__main__':
    print find_powers()
