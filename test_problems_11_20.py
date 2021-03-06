#! /usr/bin/env python


from problem11 import grid_max, grid_creator
from problem14 import problem14_version2
from problem15 import number_routs
from problem16 import power_digit_sum


def test_problem11():
    """Testing Problem 11 edge case as defined by Project Euler"""

    assert 70600674 == grid_max(grid_creator())


"""
Because of the interesting time complexity of problem 12
and the choices that could have been made to solve it the testing was
completed in the python file.

Note:
    The difference between xrange and while is negligable.
    Append versus += [] + [] was a little faster - Confirming readings
    found online.
    Concatination had no big difference on time. Not idea for reading.

"""

# Because of the simplicity of problem 13 no function formall created


def test_prblem14():
    """testing problem 14 edge case as defined by project Euler"""

    assert (837799, 524) == problem14_version2()


def test_problem15():
    """testing problem 15 edge case as defined by project Euler"""

    assert 137846528820 == number_routs()


def test_problem16():
    """testing problem 16 edge case as defined by project Euler"""

    assert 1366 == power_digit_sum()
