#! /usr/bin/env python


# attempt 1
def find_distance(a, b, c):
    """Determine if distance between three ints is equal
    assuming unsorted entries"""

    int_holder = [a, b, c]
    int_holder.sort()

    distance_1 = int_holder[1] - int_holder[0]
    distance_2 = int_holder[2] - int_holder[1]
    if distance_1 == distance_2:
        return 'They are equally spaced'
    return None


# attempt 2
def find_distance2(a, b, c):
    """Determine if distance between three ints is equal
    using average"""
    int_holder = [a, b, c]
    average = sum(int_holder)/3.0
    if average in int_holder:
        return 'They are equally spaced'
    return None


if __name__ == '__main__':
    assert find_distance(4, 6, 2) == 'They are equally spaced'
    assert find_distance2(4, 6, 2) == 'They are equally spaced'
