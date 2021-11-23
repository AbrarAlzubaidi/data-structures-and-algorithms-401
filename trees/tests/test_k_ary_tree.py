from k_ary_tree.k_ary_tree import breadthFirst, Node
import pytest

def test_breath_first(tree):
    expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'FizzBuzz', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13']
    actual = breadthFirst(tree)
    assert actual == expected

def test_breath_first_one_node_fizz():
    root =Node(3)
    expected = ["Fizz"]
    actual = breadthFirst(root)
    assert actual == expected

def test_breath_first_one_node_buzz():
    root =Node(5)
    expected = ["Buzz"]
    actual = breadthFirst(root)
    assert actual == expected

def test_breath_first_one_node_fizz_buzz():
    root =Node(75)
    expected = ["FizzBuzz"]
    actual = breadthFirst(root)
    assert actual == expected

def test_breath_first_empty_node():
    root =Node()
    with pytest.raises(Exception):
       breadthFirst(root)

@pytest.fixture
def tree():
    root = Node(1)
    root.children.append(Node(2))
    root.children.append(Node(3))
    root.children.append(Node(4)) 
    root.children[0].children.append(Node(5)) 
    root.children[0].children[0].children.append(Node(10)) 
    root.children[0].children.append(Node(6)) 
    root.children[0].children[1].children.append(Node(11))
    root.children[0].children[1].children.append(Node(12))
    root.children[0].children[1].children.append(Node(13)) 
    root.children[2].children.append(Node(15))
    root.children[2].children.append(Node(8))
    root.children[2].children.append(Node(9))
    return root
