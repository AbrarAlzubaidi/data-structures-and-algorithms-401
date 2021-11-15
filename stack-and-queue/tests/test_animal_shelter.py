from animalshelter.animal_shelter import AnimalShelter

import pytest

def test_add_cat():
    shelter = AnimalShelter()
    shelter.enqueue('cat1', 'cat')
    actual=shelter.dequeue('cat')
    expected='cat called cat1 adopted'
    assert actual == expected

def test_add_dog():
    shelter = AnimalShelter()
    shelter.enqueue('dog1', 'dog')
    actual =shelter.dequeue('dog') 
    expected = 'dog called dog1 adopted'
    assert actual == expected

def test_exception():
    shelter = AnimalShelter()
    with pytest.raises(Exception):
       shelter.dequeue() 


    