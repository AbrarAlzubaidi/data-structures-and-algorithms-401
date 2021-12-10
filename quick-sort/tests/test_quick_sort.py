from quick_sort import __version__
from quick_sort.quick_sort import quick_sort


def test_version():
    assert __version__ == '0.1.0'

def test_quick_sort():
    arr = [8,4,23,42,16,15]
    n = len(arr)
    actual=quick_sort(arr, 0, n-1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected