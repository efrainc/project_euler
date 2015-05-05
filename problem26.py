#! /usr/bin/env python


def recurring_cycle(d):
    """Using Math Therom  """
    for t in range(1, d):
        if 1 == 10**t % d:
            return t


if __name__ == '__main__':
    print max(recurring_cycle(i) for i in range(2, 1001))

