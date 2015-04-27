#! /usr/bin/env python


def read_file():
    """Opens Project Euer Name file. Reads names, sorts and converts str into
    a list object"""

    a = open('names.txt', 'r')
    data = a.read()
    names = data.split(",")
    a.close()
    names.sort()
    return names


def name_score():
    """Calculates the total name score of each name in the sorted file """

    names = read_file()
    total = 0
    for i in xrange(len(names)):
        score = 0
        for letter in names[i]:
            if letter != '"':
                score += (ord(letter) - 64)
        score = score * (i+1)
        total += score
    return total


if __name__ == "__main__":
    print name_score()
