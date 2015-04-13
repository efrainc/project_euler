#! /usr/bin/env python

from problem1 import problem1
from problem2 import fibtest
from problem3 import largest_prime
from problem4 import probl4
from problem5 import smallest_multiple
from problem6 import sum_square_difference
from problem7 import find_xprime
from problem8 import sequence_maximum, test_string, clean_string
from problem9 import pythagorean_triplet
from problem10 import sum_of_primes


def test_problem1():
    """Testing Problem one edge case
    as defined by Project Euler"""

    assert 233168 == problem1()


def test_problem2():
    """Testing Problem two edge case
    as defined by Project Euler"""

    assert 4613732 == fibtest()


def test_problem3():
    """Testing Problem three edge case
    as defined by Project Euler"""

    assert 1 == largest_prime(1)
    assert 0 == largest_prime(0)
    assert 6857 == largest_prime(600851475143)


def test_problem4():
    """Testing Problem four edge case
    as defined by Project Euler"""

    assert 906609 == probl4()


def test_problem5():
    """Testing Problem five edge case
    as defined by Project Euler"""

    assert 232792560 == smallest_multiple()


def test_problem6():
    """Testing Problem six edge case
    as defined by Project Euler"""

    assert 25164150 == sum_square_difference()


def test_problem7():
    """Testing Problem seven edge case
    as defined by Project Euler"""

    assert 104743 == find_xprime(10001)


def test_problem8():
    """Testing Problem eight edge case
    as defined by Project Euler"""
    clean = clean_string(test_string)

    assert 23514624000 == sequence_maximum(clean)


def test_problem9():
    """Testing Problem nine edge case
    as defined by Project Euler"""

    assert (200, 375, 425) == pythagorean_triplet()


def test_problem10():
    """Testing Problem ten edge case
    as defined by Project Euler"""

    assert 142913828922 == sum_of_primes(2000000)
