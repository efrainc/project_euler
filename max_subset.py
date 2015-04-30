#! /usr/bin/env python


""" return the maximum sum of a subset of a list"""

""" Assumptions
1: subset is given as a number - which will be the length of the subset
"""
import sys


def subset_max(input_list, input_subest_len):
    """Find the maxium sum of a subset in a list"""

    maximum = 0
    if input_subest_len > len(input_list):
        return "Whoop There is it == longer than list"

    for i in range(len(input_list)-input_subest_len):
        total = sum(input_list[i:(i+input_subest_len)])
        if total > maximum:
            maximum = total

    return maximum


if __name__ == "__main__":
    input_list = []
    new = sys.argv[1].split()
    for i in range(len(new)):
        input_list.append(int(new[i]))
    print subset_max(input_list, int(sys.argv[2]))
