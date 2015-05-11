#! /usr/bin/env python

"""To find the upper bound we look at the largest single digit factorial '9'
which gives us a value of 362880. The len of this number is 6 so if we have a
six digit number with all 9's that would give us 999999 -> 362880 * 6 =
2.1 Million which is seven digits. Assume all seven digits are 9 that sume is
2.5 Million which means the longest possible number we can reach with sumes is
2.5 Million and therefore our upper bound"""


def digit_facorials():
    final_list = []
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    for x in range(3, 2500000):
        string = str(x)
        total = 0
        for i in string:
            total += facts[int(i)]
        if total == x:
            final_list.append(x)
    return final_list

if __name__ == '__main__':
    print digit_facorials()