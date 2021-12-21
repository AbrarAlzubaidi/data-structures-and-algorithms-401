from collections import deque

class Stack:
  def __init__(self):
    self.stack = deque()

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    return self.stack.pop()

  def __len__(self):
    return len(self.stack)

class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.append(value)
  
  def dequeue(self):
    return self.dq.pop()
  
  def __len__(self):
    return len(self.dq)



class Vertex:
  """
  Input:Value
  What is doing: Store the value
  Return: None
  """
  def __init__(self, value):
    self.value = value

class Edge:
  """
  Input: Vertex, weight
  What is doing: Store the vertex and the weight
  Return: None
  """
  def __init__(self,vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:
  """
  Input: None
  What is doing: It is creating an empty graph 
  Return: None
  """
  def __init__(self):
    self.__adj_list = {}
    

  """
  Input : Value
  What is doing : add node to the Graph
  Return : node
  """
  def add_node(self, value):
    node = Vertex(value)
    self.__adj_list[node] = []
    return node

  """
  Input: start_vertex, end_vertex , 
  weight:optional
  What is doing: Creat an edge and append the edge to the value of
  start_vertex inside the adj_list
  Return: None
  """
  def add_edge(self, start_vertex, end_vertex, weight=0):
    if start_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    if end_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    edge = Edge(end_vertex, weight)
    self.__adj_list[start_vertex].append(edge)
    
  """
  Input : Vertex
  What is doing: Get all neighbors for a vertex
  Return: a list of edges
  """
  def get_neighbors(self, vertex):
    return self.__adj_list.get(vertex, [])
  
  

  """
  Input : None
  What is doing : get all the nodes in the graph as a set or list
  Return : a list or set of the nodes
  """
  def get_nodes(self):
    return self._adj_list.keys()

  """
  Input: None
  What is doing: find the length of the adj_list
  Return: int The size(the length of adj_list)
  """
  def size(self):
    return len(self.__adj_list)

  """
  Input: Start_vertex
  What is doing: it will traverse throught all nodes
  Return: A list of nodes
  """
  def breath_first(self, start_vertex):
    queue = Queue()
    result = []
    visited = set()

    queue.enqueue(start_vertex)
    visited.add(start_vertex)
    result.append(start_vertex.value)

    while len(queue):
      current_vertex = queue.dequeue()

      neighbors = self.get_neighbors(current_vertex)

      for edge in neighbors:
        neighbor = edge.vertex

        if neighbor not in visited:
          queue.enqueue(neighbor)
          visited.add(neighbor)
          result.append(neighbor.value)

    return result

  def depth_first(self, node):
    result=[]
    stack= Stack()
    visited= set()

    stack.push(node)
    visited.add(node.value)
    result.append(node.value)
        
    while len(stack):
      vertex=stack.pop()
      neighbors = self.get_neighbors(vertex)

      for edge in neighbors:
        neighbor = edge.vertex

        if neighbor not in visited:
          stack.push(neighbor)
          visited.add(neighbor)
          result.append(neighbor.value)
        
    return result


if __name__ == "__main__":
    graph = Graph()
    node1=graph.add_node('a')
    node2=graph.add_node('b')
    node3=graph.add_node('c')
    node4=graph.add_node('d')
    node5=graph.add_node('e')
    node6=graph.add_node('f')
    node7=graph.add_node('g')
    node8=graph.add_node('h')

    # a : b,d
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node4)

    # b:  a,d,c
    graph.add_edge(node2, node1)
    graph.add_edge(node2, node4)
    graph.add_edge(node2, node3)

    # c : b
    graph.add_edge(node3, node2)

    # g: c
    graph.add_edge(node7, node3)
   
    # d : a,b,e,f,h
    graph.add_edge(node4, node1)
    graph.add_edge(node4, node2)
    graph.add_edge(node4, node5)
    graph.add_edge(node4, node6)
    graph.add_edge(node4, node8)

    # e : d
    graph.add_edge(node5, node4)

    # f : d,h
    graph.add_edge(node6, node4)
    graph.add_edge(node6, node8)

    # h: f,d
    graph.add_edge(node8, node4)
    graph.add_edge(node8, node6)

    print('travrse:\n', graph.depth_first(node1))




