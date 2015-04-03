#! /usr/bin/env python


def find_powers():
    final = []
    for x in xrange(2, 101):
        for y in xrange(2, 101):
            final.append(x**y)
    return len(set(final))


if __name__ == '__main__':
    print find_powers()