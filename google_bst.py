#! /usr/bin/env python


"""
You are given the following code:

A Node in a binary tree.
class Node:
  def left()  returns the left child Node if it exists; returns None
              otherwise.
  def right() returns the right child Node if it exists; returns None
              otherwise.

# Determines whether a tree with root Node |root| is balanced.
# Args:
#   root: Node, the root node of the tree.
# Returns:
#   bool: Whether or not the tree is balanced.
def IsBalanced(root):
# TODO: Complete this function.
  pass
"""


class Node(object):
    def __init__(self, data, left=None, right=None):
        """Creates a node for the Bst class"""

        self.data = data
        self._left = left
        self._right = right

    def left(self):
        return self._left

    def right(self):
        return self._right

    def Isbalanced(self):
        if self.left() and self.right() is None:
            return False
        if self.right() and self.left() is None:
            return False
        else:
            print self.right()
            print self.left()
            right_depth = self.depth(self.right())
            print right_depth
            left_depth = self.depth(self.left())
            print left_depth
            if right_depth != left_depth:
                return False
            else:
                return True

    def depth(self, node, depthed=1):
        if node.left() and node.right():
            return max(self.depth(node.left(), depthed+1), self.depth(node.right(), depthed+1))
        elif node.left():
            return self.depth(node.left(), depthed+1)
        elif node.right():
            return self.depth(node.right(), depthed+1)
        else:
            return depthed


class Bst(object):
    top = None

    def __init__(self):
        """Initialize a binary search tree"""

        self.top = None
        self.set = set()

    def insert(self, val):
        """Insert a Node into the binary tree"""

        if val not in self.set:
            if self.top is None:
                self.top = Node(val)
            else:
                current = self.top
                while current:
                    if val < current.data:
                        if current.left() is None:
                            current._left = Node(val)
                            break
                        current = current._left
                    else:
                        if current.right() is None:
                            current._right = Node(val)
                            break
                        current = current._right
            self.set.add(val)

if __name__ == '__main__':
    tree = Bst()
    tree.insert(10)
    tree.insert(4)
    tree.insert(15)
    # tree.insert(3)
    # tree.insert(5)
    # tree.insert(6)
    print tree.top.Isbalanced()

