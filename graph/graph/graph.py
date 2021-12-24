class Node:
    def __init__(self, value):
        """
        input: value
        do: create a vertex
        output: none        
        """
        self.value = value

class Edge:
    def __init__(self, second_node, weight=0):
        """
        input: second node and weight
        do: store the vertex and weight for edge
        output: none
        """
        self.second_node = second_node
        self.weight = weight

class Graph:
    def __init__(self):
        """
        input: none
        do: declare an empty graph
        output: none
        """
        # afjacency list
        self.__adj_list={} # private attribute just can use it in a class, to access it you should build a method to return the private attributes

    def add_node(self, value):
        """
        input: value of vertex
        do: add a node to the graph
        output: node 
        """
        node = Node(value)
        self.__adj_list[node.value] = []
        return node

    def add_edge(self, first_node, second_node=None, weight=0):
        """
        input: first node, second node, weight
        do: add edge between 2 nodes and append the edge to the value of first node inside adj_list
        output: none
        """
        if first_node.value not in self.__adj_list:
            raise KeyError('start node is not exist !!')
        if second_node.value not in self.__adj_list:
            raise KeyError('second node is not exist !!')
        edge =Edge(second_node.value, weight)
        # print(edge.second_node)
        self.__adj_list[first_node.value].append([edge.second_node, edge.weight])

    def get_neighbors(self, node):
        """
        input: node
        do: get all nighbors for the node
        return: a list of edges
        """
        return self.__adj_list.get(node.value,[])

    def get_nodes(self):
        """
        input: none
        do: get all the nodes in the adj_list as a set or list
        output: a list or set of the nodes
        """
        return list(self.__adj_list.keys())

    def size(self):
        """
        input: none
        do: find the length of adj_list
        output: lenght/size
        """
        if len(self.__adj_list):
            return len(self.__adj_list)
        else:
            return "null"

    def get_graph(self):
        if self.__adj_list:
            return self.__adj_list
        else:
            return 'empty graph'
    
if __name__ == "__main__":
    graph = Graph()
    node1=graph.add_node(5)
    node2=graph.add_node(9)
    node3=graph.add_node(1)
    node4=graph.add_node(3)
    node5=graph.add_node(16)
    node6=graph.add_node(20)
    # node1 : node2,3,4
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    graph.add_edge(node1, node4)

    # node3: node5,6
    graph.add_edge(node3, node5)
    graph.add_edge(node3, node6)

    # node4 : node6
    graph.add_edge(node4, node6)

    print('Graph 1 \n')
    print('all nodes: ', graph.get_nodes())
    print('all neighbors for node1 (5): ', graph.get_neighbors(node1))
    print('all neighbors for node2 (9): ', graph.get_neighbors(node2))
    print('Graph 1 >>>\n',graph.get_graph())
    print('Graph 1 size: ', graph.size())
    print('*'*50)
    graph2 = Graph()
    node1_graph2=graph2.add_node(6)
    print('Graph 2 >>>\n',graph2.get_graph())
    print('Graph 2 size: ', graph2.size())
    print('*'*50)
    graph3= Graph()
    print('Graph 3 >>>\n',graph3.get_graph())
    print('Graph 3 size: ', graph3.size())
