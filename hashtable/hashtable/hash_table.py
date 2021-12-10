from types import new_class
from hashtable.linkedlist import LinkedList


class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.map = [None]*size
        # self.map = [LinkedList()]*size
        # self.map = [[]]*size

    def custom_hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            # get asci value for character
            asccii_of_ch = ord(ch)
            sum_of_asccii+= asccii_of_ch
        temp_value = sum_of_asccii*19
        index = temp_value%self.size
        return index

    def add(self, key, value):
        index = self.custom_hash(key)
        # if location is None 
        if not self.map[index]:
            self.map[index] = [key,value]
        # collision state
        else:
            # if there is already a linkedlist
            if isinstance(self.map[index], LinkedList):
                self.map[index].add([key,value])
            else:   
            # if there is no linkedlist (collision for the first time)
                chain = LinkedList()
                # if this already a value in map get it
                existing_pair = self.map[index]
                # new pair that also have to store in the same index of existing one
                new_pair =[key,value]
                # in that index store a linkedlist
                self.map[index]=chain
                # add these pairs(which causes the collesion in the linkedlsit)
                chain.add(existing_pair)
                chain.add(new_pair)

    def get_value(self, key):
        index=self.custom_hash(key)
        if(isinstance(self.map[index], LinkedList)):
            head_of_link = self.map[index]
            current = head_of_link.head
            while current:
                if current.data[0]==key:
                    print(current.data[1])
                    return current.data[1]
                current= current.next

        else:
            return self.map[index]

        return self.map[index]

    def contains(self, key):
        for value in self.map:
            if isinstance(value, LinkedList):
                current = value.head
                while current:
                    if current.data[0]==key:
                        return True
                    current= current.next
            
            if type(value) == list:
                if value[0] == key:
                    return True
        return False
if __name__ == "__main__":
    hashtable= HashTable()
    hashtable.add("AHMAD",10)
    hashtable.add("YAHYA",20)
    hashtable.add("HAMAD",30)
    hashtable.add("KEY",100)
    hashtable.get_value('YAHYA')
    print('is HAMAD exist? ',hashtable.contains('HAMAD'))
    print('='*25)
    print('index\tvalue')

    for index,value in enumerate(hashtable.map):
        if isinstance(value, LinkedList):
            current = value.head
            while current:
                print(index,'\t',current.data[1])
                current= current.next
        if type(value) == list:
            print(index,'\t', value[1])