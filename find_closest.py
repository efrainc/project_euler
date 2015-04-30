#! /usr/bin/env python


"""Modify a binary search to find the closest number to your search val
(assume input array is pre-sorted)"""

""" Assumptions
1: You are given the top of the tree.
2: You only have node.left and node.right
3: if no node exisits node.righ/left return None
4: All Values are unique (no repitition)
"""


def closest(top_node, input_num):
    """Search a tree for the node with the cloest value to the input"""

    if input_num == top_node:
        return top_node

    node = top_node
    output = (abs(node.value - input_num), node)
    while node:
        if output == 0:
            return node
        if input_num < node.vale:
            node = node.left
        else:
            node = node.right
        difference = abs(node.vale - input_num)
        if difference < output[0]:
            output = (difference, node)

    return output[1]

""" Notes
Space complexity is O(n) no recrusion or duplication of data structures.
Time complexity is O(nlogn) - BST property is nlogn
"""