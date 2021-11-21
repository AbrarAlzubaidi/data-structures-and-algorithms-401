# Trees

trees is another type of non-linear DS that its element's order you can not know it. trees is a group of nodes linked with each other by pointers

**types**
1. binart tree
2. k-th tree
3. Binary Search Tree


## Challenge

- make class tree with: 
    - pre-order method
    - in-order method 
    - post-order method

- make binary search tree calss with: 
    - add method
    - contains method

- make k-th tree with: 
    - breadth First method

## Approach & Efficiency

- class tree with: 
    - pre-order method---> time O(n)  space O(1)
    - in-order method ----> time O(n)  space O(1)
    - post-order method----> time O(n)  space O(1)

- make binary search tree calss with: 
    - add method ---> time O(h)  space O(1)
    - contains method---> time O(h)  space O(1)

- make k-th tree with: 
    - breadth First method ---> time O(n)  space O(1)

## API

- class tree with: 
    - pre-order method--->`[root, left, right]`
    - in-order method ----> `[left, root, right]`
    - post-order method----> `[left, right, root]`

- binary search tree calss with: 
    - add method ---> insert a new node to BS-tree
    - contains method---> search on node in BS-tree

- k-th tree with: 
    - breadth First method ---> search through a tree one level at a time 