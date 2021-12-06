from merge_sort import __version__
from merge_sort.merge_sort import merge_sort

def test_version():
    assert __version__ == '0.1.0'

def test_merge_sort():
    actual1 = merge_sort([8,4,23,42,16,15])
    expected1 = [4, 8, 15, 16, 23, 42]
    assert actual1 == expected1

def test_reverse_array():
    actual2 = merge_sort([20,18,12,8,5,-2])
    expected2 = [-2,5,8,12,18,20]
    assert actual2 == expected2

def test_repeated_item():
    actual3 = merge_sort([5,12,7,5,5,7])
    expected3 = [5,5,5,7,7,12]
    assert actual3 == expected3
