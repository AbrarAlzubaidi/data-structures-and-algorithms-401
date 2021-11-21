from trees.binary_tree import Tree

from trees.node import Node

import pytest

# Can successfully instantiate an empty tree
def test_empty_tree():
    tree = Tree()
    actual = str(tree)
    expected = tree.__str__()
    assert actual == expected

# Can successfully instantiate a tree with a single root node
def test_one_node_tree():
    tree = Tree()
    tree.root=Node("A")
    actual = tree.root.value
    expected = 'A'
    assert actual == expected

# Can successfully add a left child and right child to a single root node
def test_root_left_and_right_child(tree):
    actual_right = tree.root.right.value
    expected_right = 'C'
    actual_left = tree.root.left.value
    expected_left = 'B'
    assert actual_right == expected_right
    assert actual_left == expected_left

# Can successfully return a collection from a preorder traversal
def test_pre_order(tree):
    inOrder = tree.pre_order()
    actual = inOrder(tree.root)
    expected = ['A', 'B', 'C']
    assert actual == expected

# Can successfully return a collection from an inorder traversal
def test_in_order(tree):
    inOrder = tree.in_order()
    actual = inOrder(tree.root)
    expected = ['B', 'A', 'C']
    assert actual == expected

# Can successfully return a collection from a postorder traversal
def test_post_order(tree):
    inOrder = tree.post_order()
    actual = inOrder(tree.root)
    expected = ['B', 'C', 'A']
    assert actual == expected

@pytest.fixture
def tree():
    tree = Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    return tree
