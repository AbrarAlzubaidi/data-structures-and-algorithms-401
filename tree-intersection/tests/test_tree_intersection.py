from tree_intersection import __version__
from tree_intersection.tree_intersection import tree_intersection
from tree_intersection.binary_tree import Tree
from tree_intersection.node import Node

import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_tree_intersection():
    tree1=Tree()
    tree1.root=Node("A1")
    tree1.root.left=Node("B")
    tree1.root.right=Node("C")
    tree1.root.left.left=Node("D")
    tree1.root.left.right=Node("E")
    tree1.root.right.left=Node("F")

    tree2=Tree()
    tree2.root=Node("A")
    tree2.root.left=Node("B")
    tree2.root.right=Node("C")
    tree2.root.left.left=Node("D")
    tree2.root.left.right=Node("E")

    actual=tree_intersection(tree1,tree2)
    expected = ['B', 'D', 'E', 'C']
    assert actual == expected

def test_empty_trees():
    tree1=Tree()
    tree2=Tree()

    with pytest.raises(Exception):
        tree_intersection(tree1,tree2)

def test_no_intersection():
    tree1=Tree()
    tree1.root=Node("A1")
    tree1.root.left=Node("B1")
    tree1.root.right=Node("C1")
    tree1.root.left.left=Node("D1")
    tree1.root.left.right=Node("E1")

    tree2=Tree()
    tree2.root=Node("A")
    tree2.root.left=Node("B")
    tree2.root.right=Node("C")
    tree2.root.left.left=Node("D")
    tree2.root.left.right=Node("E")

    actual=tree_intersection(tree1,tree2)
    expected = 'No intersection between two trees'
    assert actual == expected
    