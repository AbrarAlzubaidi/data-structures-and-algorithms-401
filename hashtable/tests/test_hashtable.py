from hashtable import __version__
import pytest
from hashtable.hash_table import HashTable
from hashtable.linkedlist import LinkedList

def test_version():
    assert __version__ == '0.1.0'

# Adding a key/value to your hashtable results in the value being in the data structure
def test_add_keys_and_values(hash):
    result=''
    for index,value in enumerate(hash.map):
        if isinstance(value, LinkedList):
            current = value.head
            while current:
                result=result +str(current.data[1])+' '
                current= current.next
        if type(value) == list:
            result=result +str(value[1])+' '

    assert result == '20 10 30 '


# Retrieving based on a key returns the value stored
def test_contains_true(hash):
    actual = hash.contains('HAMAD')
    expected =True
    assert actual == expected

# Successfully returns null for a key that does not exist in the hashtable
def test_contains_false(hash):
    actual = hash.contains('MAD')
    expected =False
    assert actual == expected

# Successfully handle a collision within the hashtable
def test_handle_collision(hash):
    flag=False
    for index,value in enumerate(hash.map):
        if isinstance(value, LinkedList):
            flag = True
    assert flag == True

# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_get_value_from_collision(hash):
    actual = hash.get_value('AHMAD')
    expected = 10
    assert actual == expected
# Successfully hash a key to an in-range value
def test_add_hash_value(hash):
    hash.add('KEY', 100)
    result=''
    for index,value in enumerate(hash.map):
        if isinstance(value, LinkedList):
            current = value.head
            while current:
                result=result +str(current.data[1])+' '
                current= current.next
        if type(value) == list:
            result =result +str(value[1])+' '
            print(result)

    assert result == '20 100 10 30 '


@pytest.fixture
def hash():
    hashtable= HashTable()
    hashtable.add("AHMAD",10)
    hashtable.add("YAHYA",20)
    hashtable.add("HAMAD",30)
    return hashtable