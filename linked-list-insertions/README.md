# Challenge Summary
challenge has to build 3 methods:
1. append: to insert node at end
2. insert before: to insert node before specific node
3. insert after: to insert node after specific node

## Whiteboard Process
![Whiteboard](https://github.com/AbrarAlzubaidi/data-structures-and-algorithms-401/blob/main/linked-list-insertions/cha.6.PNG)
### link to Whiteboard
[Whiteboard](https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtL2YwNTI5N2I0NTkwODQxNGU5MTAxZGIyM2YyOWZmYTFmX2M3MTQyNTMxLWRkNjgtNGE2Zi1iMDM2LTAzOWVjNTJkNmJkMV9mYmYyYmQ4OC05NDI0LTQxNGMtYTNlZS01N2VjYThlNzcyM2M=)

## Approach & Efficiency
1. append---> time O(n) space O(1)
2. insert before---> time O(n) space O(1)
3. insert after---> time O(n) space O(1)
## Solution
1. append---> 

        original= "{ hi } -> { 70 } -> { 50 } -> NULL"
        linkedlist.append(4)
        expected = "{ hi } -> { 70 } -> { 50 } -> { 4 } -> NULL"
        

2. insert before---> time O(n) space O(1)

        original= "{ hi } -> { 70 } -> { 50 } -> NULL"
        linkedlist.insert_before(50,"welcome")
        expected = "{ hi } -> { 70 } -> { welcome } -> { 50 } -> NULL"
        
3. insert after---> time O(n) space O(1)

        original= "{ hi } -> { 70 } -> { 50 } -> NULL"
        linkedlist.insert_after('hi',"welcome")
        expected = "{ hi } -> { welcome } -> { 70 } -> { 50 } -> NULL"
       
