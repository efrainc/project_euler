#! /usr/bin/env python


def digit_fith_power():
    """Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits."""

    final_list = []
    for x in range(2, 350000):
        if x == sum(int(d)**5 for d in str(x)):
            final_list.append(x)
    return final_list


if __name__ == '__main__':
    print sum(digit_fith_power())