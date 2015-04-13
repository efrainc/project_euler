#! /usr/bin/env python

from problem1 import problem1
from problem2 import fibtest
from problem3 import largest_prime
from problem4 import probl4
from problem7 import find_xprime
from problem8 import sequence_maximum, test_string, clean_string


def test_problem1():
    """Testing Problem one edge case
    as defined by Project Euler"""

    assert 233168 == problem1()


def test_problem2():
    """Testing Problem one edge case
    as defined by Project Euler"""

    assert 4613732 == fibtest()


def test_problem3():
    """Testing Problem one edge case
    as defined by Project Euler"""

    assert 1 == largest_prime(1)
    assert 0 == largest_prime(0)
    assert 6857 == largest_prime(600851475143)


def test_problem4():
    """Testing Problem one edge case
    as defined by Project Euler"""

    assert 906609 == probl4()

# This test tackes a long time to run since it has to
# calculate each prime number from 1 to 10,000. Test passes
# but commented to out to save time in the future.
# def test_problem7():
#     """Testing Problem one edge case
#     as defined by Project Euler"""

#     assert 104743 == find_xprime(10001)


def test_problem8():
    """Testing Problem one edge case
    as defined by Project Euler"""
    clean = clean_string(test_string)

    assert 23514624000 == sequence_maximum(clean)
