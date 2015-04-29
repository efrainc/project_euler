#! /usr/bin/env python


def question2_1(input_list):
    """Remove duplicates from an unsorted list"""

    # easy method - call pythons set() function

    # Attach each item as input into a list. Check list for each new item

    cleaned_list = list()

    for letter in input_list:
        if letter in cleaned_list:
            pass
        else:
            cleaned_list.append(letter)

    return cleaned_list

"""
Notes - This holdes a new list in memory so we are duplicating our memory
space 2N.
Additionally, because I am using list look up we have O(n) time for each
iteration meaning this would be O(n**2) time complexity.
We can solve the time problem by using a dictonary at the cost of space.
"""


if __name__ == "__main__":
    print question2_1(['a', 'a', 'b', 'c', 'a'])
