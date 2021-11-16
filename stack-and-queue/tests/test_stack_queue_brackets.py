from stackQueueBrackets.stack_queue_brackets import validate_brackets

import pytest
def test_valid_brackets():
    actual= validate_brackets('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected


def test_invalid_brackets():
    actual= validate_brackets('{(})')
    expected = False
    assert actual == expected

def test_exception():
    with pytest.raises(Exception):
        validate_brackets()