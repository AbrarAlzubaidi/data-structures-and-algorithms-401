from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort

import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_empty_array():
     with pytest.raises(Exception):
       insertion_sort([])

def test_boolean_array():
    with pytest.raises(Exception):
        insertion_sort([1,2,3,False])

def test_string_array():
    with pytest.raises(Exception):
        insertion_sort([1,2,3,"False"])

def test_insertion_sort():
    actual = insertion_sort([8,4,23,42,16,15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

