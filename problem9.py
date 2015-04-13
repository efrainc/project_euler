#! /usr/bin/env python


def pythagorean_triplet():
    """Find the pythagorean triplet whos sum is 1000
    can but further optimized using a math equlity.
    which is beyond the scope of the proble"""

    for a in xrange(1, 700):
        for b in xrange(1, 700):
            for c in xrange(1, 700):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a, b, c


if __name__ == "__main__":
    print pythagorean_triplet()

