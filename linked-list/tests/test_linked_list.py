from linked_list import __version__

from linked_list.linked_list import Node,Linked_list

import pytest

def test_version():
    assert __version__ == '0.1.0'

# Can successfully instantiate an empty linked list
def test_empty_list():
    link_list=Linked_list()
    expected = None
    actual= link_list.head
    assert actual == expected

# Can properly insert into the linked list
def test_insert():
    link_list=Linked_list()
    link_list.insert_at_beginning(50)
    expected="{ 50 } -> NULL"
    actual=link_list.__str__()
    assert actual== expected

# The head property will properly point to the first node in the linked list
def test_head(linkedlist):
    expected="hi"
    actual=linkedlist.head.value
    assert expected==actual


# Can properly insert multiple nodes into the linked list
def test_insert_4_nodes(linkedlist):
    expected="{ hi } -> { 70 } -> { 50 } -> NULL"
    actual=linkedlist.__str__()
    assert actual== expected

# Will return true when finding a value within the linked list that exists
def test_is_include_50(linkedlist):
    expected=True
    actual=linkedlist.is_include(50)
    assert actual== expected

# Will return false when searching for a value in the linked list that does not exist
def test_is_include_6(linkedlist):
    expected=False
    actual=linkedlist.is_include(6)
    assert actual== expected

# Can properly return a collection of all the values that exist in the linked list
def test_prit_list(linkedlist):
    expected="{ hi } -> { 70 } -> { 50 } -> NULL"
    actual=linkedlist.__str__()
    assert actual== expected

@pytest.fixture
def linkedlist():
    link_list=Linked_list()
    link_list.insert_at_beginning(50)
    link_list.insert_at_beginning(70)
    link_list.insert_at_beginning('hi')
    return link_list









