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
    
    def merge(self, p=None, q= None):
        if p == None or q==None:
            raise Exception('you entered one limked-list please enter 2 linked-lists') 
        else:
            current1 = p.head
            current2 = q.head

            # swap their positions until one finishes off
            while current1 != None and current2 != None:
                # if q length > p length
                if current1.next == None:
                    current1.next = current2
                    break

                # if p length > q length
                if current2 == None:
                    current1.next = current2
                    break

                # if q length = p length
                else:
                    # Save next pointers
                    p_next = current1.next
                    q_next = current2.next
        
                    # make current2 as next of current1
                    current2.next = p_next  # change next pointer of current2
                    current1.next = current2  # change next pointer of current1
        
                    # update current pointers for next iteration
                    current1 = p_next
                    current2 = q_next
                    q.head = current2


    def kFromEnd(self, k):
        """
        this method for return the nth index in the linked-list from end of it
        """
        count =0
        current = self.head
        while current:
            current = current.next
            count = count + 1
        k+=1
        if count==1:
            return self.head.value
        else:
            while k>0 and k<count:
                if count >= k:
                    current = self.head
                    # this for loop i take it from techiedelight.com it helps me ^^
                    for i in range(count - k):
                        current = current.next
                    return current.value
            if k<=0:
                    return 'you entered a negative index'
            if k-1 == count:
                return f'you have to enter a number between 0 and {count}'
            if k>count:
                return 'you enter a number biggest than length of the liked-list'
            
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


    def insert_before(self,value,newVal):   # (value to add before it, the new value to add)
        """
        this method to insert a new node before a specific node
        """
        newNode=Node(newVal)
        current=self.head

        # if linked list is not empty
        if current is not None:
            
            # insert if linked list hold
            while current.next is not None:
                # insert if the value = to the first node in linked list
                if current.value == value:
                    newNode.next=self.head
                    self.head=newNode
                    break
                if current.next.value == value:
                    newNode.next = current.next
                    current.next = newNode
                    break
                    
                else:
                    current = current.next


    def insert_after(self, value, newVal):
        """
        this method to insert a new node after a specific node
        """
        newNode= Node(newVal)
        current=self.head

        if current is not None: 
            
            while current.next is not None:
                if current.value == value:
                    newNode.next= current.next
                    current.next = newNode
                    break
                else:
                    current =current.next

            if current.next == None:
                current.next = newNode


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
            while current:
                result += "{ "+f"{current.value}"+" } -> "
                current = current.next
        result += "NULL"
        return result


def zipLists(p = None, q = None):
    if p == None or q==None:
            raise Exception('you entered one limked-list please enter 2 linked-lists') 
    else:
        current1 = p.head
        current2 = q.head

        # swap their positions until one finishes off
        while current1 != None and current2 != None:
            # if q length > p length
            if current1.next == None:
                current1.next = current2
                break

            # if p length > q length
            if current2 == None:
                current1.next = current2
                break

            # if q length = p length
            else:
                # Save next pointers
                p_next = current1.next
                q_next = current2.next
        
                # make current2 as next of current1
                current2.next = p_next  # change next pointer of current2
                current1.next = current2  # change next pointer of current1
        
                # update current pointers for next iteration
                current1 = p_next
                current2 = q_next
                q.head = current2



if __name__ == "__main__":
    l1 = Linked_list()
    l2 = Linked_list()
    l3 = Linked_list()

    l1.append(1)
    l1.append(3)
    l1.append(2)

    l2.append(5)
    l2.append(9)
    l2.append(4)

    print('first list: ',l1)
    print('second list: ',l2)
    #  l1.merge(l1,l2)
    #  print('merge lists: ',l1)
    zipLists(l1,l2)
    print('lists after zipped',l1)