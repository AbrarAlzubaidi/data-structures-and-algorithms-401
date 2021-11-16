# Challenge Summary
stack_queue_brackets to check if group of brackets are match or not (return boolean value)

    Ex: {}(){}----> match

        [({}] ----> not match

## Whiteboard Process

[whiteboard](https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtLzliNDVkMDQwZTMzNTQyNzhhOGM0M2Y1MTE0Zjg3NTgzX2M3MTQyNTMxLWRkNjgtNGE2Zi1iMDM2LTAzOWVjNTJkNmJkMV9kZWE5ZmE2NS0zNGJlLTQ5OGUtODA3NS01ZGFlODZhMjNhMjE=)

![whiteboard]()
## Approach & Efficiency
stack implimitation push, pop, peek (LIFO)

- big O:
1. time: O(n)
2. space: O(n)

## Solution

- valid: 

        actual= validate_brackets('{}{Code}[Fellows](())')
        expected = True
        assert actual == expected

- invalid: 

        actual= validate_brackets('{(})')
        expected = False
        assert actual == expected
