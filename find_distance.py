#! /usr/bin/env python


# attempt 1
def find_distance(a, b, c):
    """Determine if distance between three ints is equal"""

    distance_1 = b - a
    distance_2 = c - b
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
    assert find_distance(2, 4, 6) == 'They are equally spaced'
    assert find_distance2(20, 40, 60) == 'They are equally spaced'
