from trees.node import Node
from trees.binary_tree import Tree

import pytest
def test_get_max(tree):
    actual= tree.get_max(tree.root)
    expected = 78
    assert actual == expected

    

@pytest.fixture
def tree():
    tree = Tree()
    #level 0
    tree.root = Node(40)
    #level 1
    tree.root.left = Node(10)
    tree.root.right = Node(11)
    #level 2
    tree.root.left.left = Node(78)
    tree.root.left.right = Node(46)
    tree.root.right.right = Node(9)
    return tree
