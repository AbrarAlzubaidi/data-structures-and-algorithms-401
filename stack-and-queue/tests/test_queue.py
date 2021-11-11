from stack_and_queue.queue import Queue

import pytest

# Can successfully enqueue into a queue
def test_enqueue():
    queue =Queue()
    queue.enqueue(1)
    expected = 1
    actual = queue.rear.value
    assert expected == actual

# Can successfully enqueue multiple values into a queue
def test_enqueue_muti(queue_data):
    expected = 3
    actual = queue_data.rear.value
    assert expected == actual

# Can successfully dequeue out of a queue the expected value
def test_dequeue(queue_data):
    expected = 1
    actual = queue_data.dequeue()
    assert expected == actual

# Can successfully peek into a queue, seeing the expected value
def test_peek(queue_data):
    expected = 1
    actual = queue_data.peek()
    assert expected == actual

# Can successfully empty a queue after multiple dequeues
def test_dequeue_till_empty_queue(queue_data):
    expected = None
    queue_data.dequeue()
    queue_data.dequeue()
    queue_data.dequeue()
    actual = queue_data.front
    assert expected == actual

# Can successfully instantiate an empty queue
def test_empty_queue():
    queue =Queue()
    expected = None
    actual = queue.front
    assert expected == actual
    
# Calling dequeue or peek on empty queue raises exception
def test_exception():
    queue =Queue()
    with pytest.raises(Exception):
       queue.dequeue() 

@pytest.fixture
def queue_data():
    queue =Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue