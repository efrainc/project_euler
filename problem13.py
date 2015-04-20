#! /usr/bin/env python


if __name__ == '__main__':
    a = open('problem13_input.txt', 'r')
    output = 0
    for line in a:
        output += int(line)

    print output
