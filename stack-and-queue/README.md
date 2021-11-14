# Stacks and Queues
**stack** is a conceptual structure consisting of a set of homogeneous elements and is based on the principle of last in first out (LIFO)

**Queue** is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO)

## Challenge

**challenge-10**

- to add stack methods as: 

    1. push
    2. pop
    3. peek
    4. is empty
    and test it

- to add queue methods as: 

    1. enqueue
    2. dequeue
    3. peek
    4. is empty
    and test it

**challenge-11**

- to implements queue using stack:

    1. enqueue using push and peek
    2. dequeue  using push and pop

## Whiteboard Process

**challenge-11**

![whiteboard]()

[whiteboard](https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtL2Q5MzE0N2Y3NjI2ZjQ4M2FhYTgxNjgwMjgzMjQ5NmU5X2M3MTQyNTMxLWRkNjgtNGE2Zi1iMDM2LTAzOWVjNTJkNmJkMV9hY2RjZDgwNC1mZWRkLTQyOGQtOWZjNC00YThhYmE4ZGViZGE=)

## Approach & Efficiency

**challenge-10**

- stack : 
    1. push: O(1)
    2. pop: O(1)
    3. peek: O(1) 
    4. is empty: O(1)

- queue : 
    1. enqueue: 
    2. dequeue: O(1)
    3. peek: O(1)
    4. is empty: O(1)

**challenge-11**

A) enqueue:
- time: O(n)
- space: O(1)

B) dequeue:
- time: O(n)
- space: O(1)

## API

**challenge-10**

- stack : 

    1. push: O(1)

            stack =Stack()
            stack.push(1) # add item to stack
            expected = 1
            actual = stack.tos.value
            assert expected == actual

    2. pop: O(1)

            expected = 1
            actual = stack.pop() # remove from stack
            assert expected == actual

    3. peek: O(1) 

            stack =Stack()
            stack.push(1)
            expected = 1
            actual = stack.peek() # return the value that tos points at
            assert expected == actual

    4. is empty: O(1)

            stack =Stack()
            actual = stack.is_empty() # when tos=None
            expected = True
            assert expected == actual


- queue : 

    1. enqueue: O(1)

            queue =Queue()
            queue.enqueue(1) # add item to the beginning of queue
            expected = 1
            actual = queue.rear.value
            assert expected == actual

    2. dequeue: O(1)

            expected = 1
            actual = queue.dequeue() # remove from the end of queue
            assert expected == actual

    3. peek: O(1)

            queue =Queue()
            queue.enqueue(1)
            expected = 1
            actual = queue.peek() # return the value that front points at
            assert expected == actual

    4. is empty: O(1)

            queue =Queue()
            actual = queue.is_empty() # when front=None
            expected = True
            assert expected == actual


**challenge-11**

A) enqueue:

- original queue: [10]->[15]->[20]

- enqueue(5)

- after calling the function: 
[5]->[10]->[15]->[20]


B) dequeue:

- original queue: [5]->[10]->[15]->[20]

- dequeue()

- after calling the function
20