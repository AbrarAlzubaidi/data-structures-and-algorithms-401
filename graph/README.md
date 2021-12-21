# Graphs
graphs is a non-linear DS similar of trees

**contains:**

1. nodes/ vertices
2. edges: to connect each node with another node/nodes

<h3 style = 'color:#C84B31'>Types</h3>

1. directed
2. un-directed
3. weighted
4. un-weighted
5. circlic
6. Acirclic
7. complete
8. connected
9. disconnected

<h3 style = 'color:#C84B31'>Implemetation</h3>

1. Adjacency matrix
2. Adjacency list

<h3 style = 'color:#C84B31'>Traversal</h3>

1. Breadth first
2. Depth First 


## Challenge
Implement Graph with methods: 
1. add node
2. add edge
3. get nodes
4. get neighbors
5. size

## Approach & Efficiency
1. add node:
    - time: `O(1)`
    - space: `O(1)`

2. add edge
    - time: `O(1)`
    - space: `O(1)`

3. get nodes
    - time: `O(1)`
    - space: `O(1)`

4. get neighbors
    - time: `O(1)`
    - space: `O(1)`

5. size
    - time: `O(1)`
    - space: `O(1)`



## API
1. add node

    - Arguments: value
    - Returns: The added node
    - Add a node to the graph

2. add edge

    - Arguments: 2 nodes to be connected by the edge, weight (optional)
    - Returns: nothing
    - Adds a new edge between two nodes in the graph
    - If specified, assign a weight to the edge
    - Both nodes should already be in the Graph

3. get nodes

    - Arguments: none
    - Returns all of the nodes in the graph as a collection (set, list, or similar)
    
4. get neighbors

    - Arguments: node
    - Returns a collection of edges connected to the given node
    Include the weight of the connection in the returned collection

5. size

    - Arguments: none
    - Returns the total number of nodes in the graph