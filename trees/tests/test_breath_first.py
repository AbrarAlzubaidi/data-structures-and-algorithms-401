from treeBreathFirst.tree_breadth_first import breadthFirst
from trees.node import Node
from trees.binary_tree import Tree

import pytest

def test_breath_first_binary_tree(tree):
    actual = breadthFirst(tree.root)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected

@pytest.fixture
def tree():
    tree = Tree()
    #level 0
    tree.root = Node(2)
    #level 1
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    #level 2
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.right.right = Node(9)
    #level 3
    tree.root.left.right.right = Node(11)
    tree.root.left.right.left = Node(5)
    tree.root.right.right.left = Node(4)
    return tree
