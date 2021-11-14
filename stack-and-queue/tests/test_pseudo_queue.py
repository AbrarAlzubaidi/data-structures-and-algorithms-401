from stack_and_queue.pseudo_queue import Pseudo_Queue

from stack_and_queue.stack import Stack

import pytest

def test_enqueu(data):
    actual = data.enqueue(5)
    expected = "[5]->[10]->[15]->[20]"
    assert actual == expected

def test_dequeue(data):
    actual = data.dequeue()
    expected = 20
    assert actual == expected

@pytest.fixture
def data():
    stack= Stack()
    stack.push(20)
    stack.push(15)
    stack.push(10)
    pseudo_queue = Pseudo_Queue(stack)
    return pseudo_queue