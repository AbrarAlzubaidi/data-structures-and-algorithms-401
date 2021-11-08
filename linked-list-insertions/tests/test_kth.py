from linked_list_insertions.linked_list import Node , Linked_list

import pytest

# Where k is greater than the length of the linked list
def test_k_greater_than_length(linkedlist):
    lenght=3
    expected = 'you enter a number biggest than length of the liked-list'
    actual = linkedlist.kFromEnd(4)
    assert expected == actual

# Where k and the length of the list are the same
def test_k_same_with_length(linkedlist):
    lenght=3
    expected = f'you have to enter a number between 0 and 3'
    actual = linkedlist.kFromEnd(3)
    assert expected == actual

# Where k is not a positive integer
def test_k_is_negative(linkedlist):
    lenght=3
    expected = 'you entered a negative index'
    actual = linkedlist.kFromEnd(-1)
    assert expected == actual

# Where the linked list is of a size 1
def test_list_of_one_node():
    ll=Linked_list()
    ll.append(10)
    expected = 10
    actual = ll.kFromEnd(0)
    assert expected == actual

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_kth_index(linkedlist):
    lenght=3
    expected = 70
    actual = linkedlist.kFromEnd(1)
    assert expected == actual

@pytest.fixture
def linkedlist():
    ll = Linked_list()
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(70)
    ll.insert_at_beginning('hi')
    return ll