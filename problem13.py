#! /usr/bin/env python


if __name__ == '__main__':
    """Pretty Self Explanitory  - but for completeness
    reads the file line by line. Converts each line into an int
    and add the int to a cummulative sum"""

    a = open('problem13_input.txt', 'r')
    output = 0
    for line in a:
        output += int(line)
    a.close()
    print output


"""
Thoughs:
    Could have saved each item as a variable and then run the sum
    command. But this would have taken more space.

"""
