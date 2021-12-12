from hashtable.hash_table import HashTable


def repeated_word(string =''):
    string=string.replace(',','').lower()
    string=string.replace('.','').lower()
    str_list=string.split()
    # print(str_list) -> ['once', 'upon', 'a', 'time', 'there', 'was', 'a', 'brave', 'princess', 'who']
    hash_table=HashTable()

    if string == '':
        raise Exception('empty string !!') 
    first_repeated=''
    for item in str_list:
        if hash_table.contains(item):
            first_repeated = item
            break
        else:
            hash_table.add(item,item)
    if first_repeated == "":
        return 'no repeated word in the sting'
    else:
        return first_repeated
print(repeated_word(""))