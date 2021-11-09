from linked_list_insertions.linked_list import Node , Linked_list

import pytest

# if list-1 length = list-2 length:
def test_equal_lists(linkedlist1 , linkedlist2):
    expected = '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL' 
    linkedlist1.merge(linkedlist1, linkedlist2)
    actual= linkedlist1.__str__()
    assert expected == actual

# if list-1 length > list-2 length:
def test_list1_greater(linkedlist1 , linkedlist2):
    linkedlist1.append(6)
    expected = '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> { 6 } -> NULL' 
    linkedlist1.merge(linkedlist1, linkedlist2)
    actual= linkedlist1.__str__()
    assert expected == actual

# if list-1 length < list-2 length:
def test_list2_greater(linkedlist1 , linkedlist2):
    linkedlist2.append(6)
    expected = '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> { 6 } -> NULL' 
    linkedlist1.merge(linkedlist1, linkedlist2)
    actual= linkedlist1.__str__()
    assert expected == actual

@pytest.fixture
def linkedlist1():
    l1 = Linked_list()
    l1.append(1)
    l1.append(3)
    l1.append(2)
    return l1

@pytest.fixture
def linkedlist2():
    l2 = Linked_list()
    l2.append(5)
    l2.append(9)
    l2.append(4)
    return l2