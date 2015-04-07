#! /usr/bin/env python


def proebl4():
    biggest = 0
    for i in xrange(101, 1000):
        for j in xrange(101, 1000):
            output = i * j
            if str(output) == str(output)[::-1] and output > biggest:
                biggest = output
    return biggest


if __name__ == '__main__':
    print proebl4()

