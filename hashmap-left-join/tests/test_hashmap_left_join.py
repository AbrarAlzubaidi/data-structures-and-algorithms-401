from hashmap_left_join import __version__
from hashmap_left_join.left_join import left_join
from hashmap_left_join.hash_table import HashTable
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_left_join(hash_tables):
    actual = left_join(hash_tables[0], hash_tables[1])
    expected = [['wrath', 'anger', 'delight'], ['outift', 'grab', 'NULL'], ['diligent', 'employed', 'idle'], ['guide', 'usher', 'follow'], ['fond', 'enamored', 'averse']]
    assert actual == expected

def test_empty_left_table():
    hash_table1= HashTable()
    hash_table2 =HashTable()
    hash_table2.add('fond', 'averse')
    hash_table2.add('wrath', 'delight')

    with pytest.raises(Exception):
        left_join(hash_table1, hash_table2)

def test_no_join():
    hash_table1= HashTable()
    hash_table2 =HashTable()
    hash_table1.add('diligent', 'employed')
    hash_table1.add('outift', 'grab')

    hash_table2.add('fond', 'averse')
    hash_table2.add('wrath', 'delight')
    actual = left_join(hash_table1, hash_table2)
    expected =[['outift', 'grab', 'NULL'], ['diligent', 'employed', 'NULL']]
    assert actual == expected



@pytest.fixture
def hash_tables():
    hash_table1= HashTable()
    hash_table2 =HashTable()

    # word strings as keys, and a synonym of the key as values.
    hash_table1.add('fond', 'enamored')
    hash_table1.add('wrath', 'anger')
    hash_table1.add('diligent', 'employed')
    hash_table1.add('outift', 'grab')
    hash_table1.add('guide', 'usher')

    # word strings as keys, and a antonyms of the key as values.
    hash_table2.add('fond', 'averse')
    hash_table2.add('wrath', 'delight')
    hash_table2.add('diligent','idle')
    hash_table2.add('guide','follow')
    hash_table2.add('flow','jam')

    return [hash_table1, hash_table2]