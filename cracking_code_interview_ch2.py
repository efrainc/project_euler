# Code is Sudo Code as needed and Python where possible


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


def question2_2(input_list, kth):
    """Find the kth to last element of a singly linked list"""
    # Given the first node and we do not know the size

    count = 0
    node = top # fictional name place holder
    while count < kth:
        node = node.next
        count += 1
    node_we_want = top
    while node != None:
        node = node.next
        node_we_want = node_we_want.next

    return node_we_want


def question2_3(input_list, node):
    """Deletes the input node from the list - accomplished be converting the
    current node into the next node and deleting the next node"""

    # Check to make sure at least two nodes exisit after this node
    if node.next and node.next.next:
        node.data = node.next.data
        node.next.data = None
        pointer_holder = node.next.pointer
        node.next.pointer = None
        node.pointer = pointer_holder



if __name__ == "__main__":
    print question2_1(['a', 'a', 'b', 'c', 'a'])
