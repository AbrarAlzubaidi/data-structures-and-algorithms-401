from stack_and_queue.stack import Stack

import pytest


import unittest
# Can successfully push onto a stack
def test_push():
    stack =Stack()
    stack.push(1)
    expected = 1
    actual = stack.tos.value
    assert expected == actual

# Can successfully push multiple values onto a stack
def test_push_multi_value(stack_data):
    expected = 3
    actual = stack_data.tos.value
    assert expected == actual

# Can successfully pop off the stack
def test_pop(stack_data):
    expected = 3
    actual = stack_data.pop()
    assert expected == actual

# Can successfully empty a stack after multiple pops    
def test_pop_till_empty_stack(stack_data):
    expected = None
    stack_data.pop()
    stack_data.pop()
    stack_data.pop()
    actual = stack_data.tos
    assert expected == actual

# Can successfully peek the next item on the stack
def test_peek(stack_data):
    expected = 3
    actual = stack_data.peek()
    assert expected == actual

# Can successfully instantiate an empty stack
def test_is_empty():
    stack =Stack()
    actual = stack.is_empty()
    expected = True
    assert expected == actual

# Calling pop or peek on empty stack raises exception
def test_exception():
    stack =Stack()
    with pytest.raises(Exception):
       stack.pop() 
        

@pytest.fixture
def stack_data():
    stack =Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack