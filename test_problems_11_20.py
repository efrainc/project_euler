#! /usr/bin/env python


from problem11 import grid_max, grid_creator


def test_problem11():
    """Testing Problem 11 edge case
    as defined by Project Euler"""

    assert 70600674 == grid_max(grid_creator())

