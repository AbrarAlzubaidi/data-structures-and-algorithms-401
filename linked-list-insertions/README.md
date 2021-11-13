# Challenge Summary
challenge has to build 3 methods:
1. append: to insert node at end
2. insert before: to insert node before specific node
3. insert after: to insert node after specific node
4. kth from end: to find the value that in specific index from end of linked-list
5. zip-2-linked-lists: to merge 2 linked-lists together as zip technique

## Whiteboard Process

**challenge-6**

![Whiteboard](https://github.com/AbrarAlzubaidi/data-structures-and-algorithms-401/blob/main/linked-list-insertions/cha.6.PNG)

**challenge-7**

![whiteboard](https://github.com/AbrarAlzubaidi/data-structures-and-algorithms-401/blob/main/linked-list-insertions/cha.7.PNG)


**challenge-8**

![whiteboard](https://github.com/AbrarAlzubaidi/data-structures-and-algorithms-401/blob/main/linked-list-insertions/cha.8.PNG)

### link to Whiteboard

**challenge-6**

[Whiteboard](https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtL2YwNTI5N2I0NTkwODQxNGU5MTAxZGIyM2YyOWZmYTFmX2M3MTQyNTMxLWRkNjgtNGE2Zi1iMDM2LTAzOWVjNTJkNmJkMV9mYmYyYmQ4OC05NDI0LTQxNGMtYTNlZS01N2VjYThlNzcyM2M=)

**challenge-7**
[whiteboard](https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtL2E0NmM5MWYyYTQzMjQzNTk5MGMwYTllYzRiOGExOTA0X2M3MTQyNTMxLWRkNjgtNGE2Zi1iMDM2LTAzOWVjNTJkNmJkMV9kZDgxNDg3YS1kNWM0LTRmNTMtOTljYS1hMWM4NzYzZmRiMDQ=)

**challenge-8**
[whiteboard](https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtLzIzMThkZGNkNTU1MjQ0OTc4YzZlMjAxMDVkMDY1YjRmX2M3MTQyNTMxLWRkNjgtNGE2Zi1iMDM2LTAzOWVjNTJkNmJkMV9hYTYxOWFiNy03NmRjLTRiMDgtYjIxMy0zMmMwYWMzOTI3MWU=)

## Approach & Efficiency
1. append---> time O(n) space O(1)
2. insert before---> time O(n) space O(1)
3. insert after---> time O(n) space O(1)
4. kth from end----> time O(n^2)  space(n)
5. zip-2-linked-lists----->O(n*m)  space(1)

which n: is the length of the first linked-list
m: is the length of the second linked-list


## Solution
1. append--->method 

        original= "{ hi } -> { 70 } -> { 50 } -> NULL"
        linkedlist.append(4)
        expected = "{ hi } -> { 70 } -> { 50 } -> { 4 } -> NULL"
        

2. insert before--->method

        original= "{ hi } -> { 70 } -> { 50 } -> NULL"
        linkedlist.insert_before(50,"welcome")
        expected = "{ hi } -> { 70 } -> { welcome } -> { 50 } -> NULL"
        
3. insert after--->method

        original= "{ hi } -> { 70 } -> { 50 } -> NULL"
        linkedlist.insert_after('hi',"welcome")
        expected = "{ hi } -> { welcome } -> { 70 } -> { 50 } -> NULL"


3. kth from end----->method

        ll = Linked_list()
        ll.insert_at_beginning(50)
        ll.insert_at_beginning(70)
        ll.insert_at_beginning('hi')
        original= "{ hi } -> { 70 } -> { 50 } -> NULL"
        expected = 70
        actual = linkedlist.kFromEnd(1)
        assert expected == actual

4. zip-2-linked-lists----->function


        expected = '{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL' 
        zipLists(linkedlist1, linkedlist2)
        actual= linkedlist1.__str__()
        assert expected == actual


