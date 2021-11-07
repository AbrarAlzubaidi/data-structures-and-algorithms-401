## Singly Linked List
linked list is a type of DS similar to arrays created by chain of nodes
has 2 pointer: 
1. head which points to the first node
2. next which points to the next node

## Challenge
challenge was to make a linked list and add: 
1. insert from begining method:
 to insert to an empty or an existing linked list from begining 
2. includes methos: return true if value in the linked list false if it is not
3. print: to print the whole linked list

## Approach & Efficiency
1. insert from begining method:
 O(1): cause the insertion didnt have to loop through the whole linked list
2. includes methos:
O(n): cause the insertion have to loop through the whole linked list to find the value
3. print: 
O(n): cause we print the whole linked list 

## API
1. insert from begining: 
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

2. include method: 
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

3. print method: 
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