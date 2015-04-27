#! /usr/bin/env python


from problem21 import amicable_numbers


def test_problem21():
    """testing problem 21 edge case as defined by project Euler"""

    assert 31626 == sum(amicable_numbers())

