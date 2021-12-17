from collections import deque
from graph.graph import Graph
class Queue:
    def __init__(self):
        self.queue = deque() 

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()

    def __len__(self):
        return len(self.queue) 

    def is_empty(self):
        return self.queue == []
    
def breath_first(start_node):
    """
    input: start node
    do: iterate on the graph
    output: list of nodes that inside graph
    """
    q = Queue()
    g = Graph()
    output = []
    visited = set()
    q.enqueue(start_node)
    visited.add(start_node)
    output.append(start_node)

    while len(q):
        current_node = q.dequeue()
        nighbors = g.get_neighbors(current_node)

        for edge in nighbors:
            nighbor = edge.second_node
            if nighbor not in visited:
                visited.add(nighbor)
                q.enqueue(nighbor)
                output.append(nighbor)

    return output

