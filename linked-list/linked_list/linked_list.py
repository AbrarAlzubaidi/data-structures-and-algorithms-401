class Node():
    # this calss for create a node with value and a default value for next pointer = None
    def __init__(self,value):
        self.value=value
        self.next=None


class Linked_list(): 
    # this calss for the whole linked-list as initial value for head pointer that will point to the first node = None
    count =0
    def __init__(self):
        self.head=None

    def append(self, value):
        """
        this methos for add a node either for an empty list or add from end to an existing list
        
        steps:
        1. so at first create a new node by calling the Node class
        2. and then check if the list is empty or not by checking head value if it is None that mean it is an empty so make
            the head pointer point to the node
        3. if it is not an empty then 
           a. make the current pointer pointes at the first node which head points at also 
           b. loop through the list till you reach when the next pointer = None which means it is the last node in the list
           c. after finishing looping process make the last next in the list pointes to the new node

        **Conclusion**:
           
           this function to add a new node for an empty list or at the end of an existing list
        
        """
        node = Node(value)
        Linked_list.count+=1
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def insert_at_beginning(self, value):

        """
        this methos for add a node either for an empty list or add at begining for an existing list
        
        steps:
        1. so at first create a new node by calling the Node class
        2. and then check if the list is empty or not by checking head value if it is None that mean it is an empty so make
            the head pointer point to the node
        3. if it is not an empty then 
           a. make the next pointer for the new node pointes at head of the list 
           b. then make the head pointes at the new node
           

        **Conclusion**:
           
           this function to add a new node for an empty list or at the begining of an existing list
        """
        node =Node(value)
        Linked_list.count+=1
        if self.head == None:
            self.head = node
        else:
            node.next=self.head
            self.head=node

    def is_include(self,searchedValue):

        """
        this methos for searching about value/node if it is exist then return true else return false
        
        steps:
        1. declare current pointer and assign to it the first node which is head
        2. looping through the 
            the head pointer point to the node
        3. if it is not an empty then 
           a. make the next pointer for the new node pointes at head of the list 
           b. then make the head pointes at the new node
           

        **Conclusion**:
           
           this function for searching about value return true if it is in the list else return false
        """
        current=self.head
        while current:
            if current.value == searchedValue:
                return True
             
            current=current.next
        return False
        

    def __str__(self):

        """
        this methos for print the linked list
        
        steps:
        1. declare result which for begining an empty string
        2. if the head of linked list in none which is empty then retun "an empty linked list"
        3. if it is not an empty then 
           a. declare current variable to hold the first node which is the head points at 
           b. loop through the list 
           c. re-assign the result for the value of the node
           d. move the current to the next node
           e. after finishing looping add to result a Null value to match the requirments
           f. the last step is return the result which this one holds all values inside the list
           

        **Conclusion**:
           
           this function to print the whole list if it is not empty else print "an empty list"
        """
        result = ""
        if self.head is None:
            result = "An empty linked list"
        else:
            current = self.head
            print(current)
            while current:
                print(current.value)
                result += "{ "+f"{current.value}"+" } -> "
                current = current.next
        result += "NULL"
        return result


if __name__ == "__main__":
     ll = Linked_list()
     ll.insert_at_beginning(440)
     ll.insert_at_beginning(40)
     ll.insert_at_beginning(30)
     ll.insert_at_beginning(20)
     print(ll)
     

    
