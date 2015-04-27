#! /usr/bin/env python


def generate_factors_sum():
    """Create a list of numbers and their factors from 1 - 10000"""

    number_sum = {1: 1, }
    for i in xrange(2, 10000):
        sum_divisors = 0
        for x in xrange(1, i/2+1):
            if i % x == 0:
                sum_divisors += x
        number_sum[i] = sum_divisors

    return number_sum


def amicable_numbers():
    """Check the genearted list for amicable numbers"""

    numbers = generate_factors_sum()
    list_amicable_numbers = []
    for x, y in numbers.iteritems():
        if x != y & y < 10000:
            if x == numbers[y]:
                list_amicable_numbers.append(x)
    return list_amicable_numbers


if __name__ == '__main__':
    print sum(amicable_numbers())


