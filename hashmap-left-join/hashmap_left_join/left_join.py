from hashmap_left_join.hash_table import HashTable
from hashmap_left_join.linkedlist import LinkedList
def left_join(hash1, hash2):
    data=[]

    for index,value in enumerate(hash1.map):
        if type(value) == list:
            if hash2.contains(value[0]):
                getting_data=hash2.get_value(value[0])
                data+=[[value[0],value[1],getting_data[1]]]
            else:
                data+=[[value[0], value[1], 'NULL']]

    if data== []:
        raise Exception('table one (synonym) is empty')

    return data


if __name__ == '__main__':
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

    print(left_join(hash_table1, hash_table2))
    