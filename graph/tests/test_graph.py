from sys import exec_prefix
from types import AsyncGeneratorType
from graph import __version__
from graph.graph import Graph
import pytest
def test_version():
    assert __version__ == '0.1.0'

# Node can be successfully added to the graph
def test_add_node():
    graph = Graph()
    graph.add_node(5)
    actual = graph.get_graph()
    expected = {5: []}
    assert actual == expected
# An edge can be successfully added to the graph
def test_add_edge(graph):
    actual = graph.get_graph()
    expected = {5: [[9, 0], [1, 0], [3, 0]], 9: [], 1: [[16, 0], [20, 0]], 3: [[20, 0]], 16: [], 20: []}
    assert actual == expected

# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes(graph):
    actual = graph.get_nodes()
    expected =  [5, 9, 1, 3, 16, 20]
    assert actual == expected

# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
def test_get_neighbors(graph):
    graph = Graph()
    node1=graph.add_node(5)
    node2=graph.add_node(9)
    graph.add_edge(node1, node2)
    actual = graph.get_neighbors(node1)
    expected = [[9, 0]]
    assert actual == expected

# The proper size is returned, representing the number of nodes in the graph
def test_get_size(graph):
    actual = graph.size()
    expected = 6
    assert actual == expected

# A graph with only one node and edge can be properly returned
def test_add_one_node():
    graph = Graph()
    graph.add_node(10)
    actual = graph.get_graph()
    expected = {10:[]} 
    assert actual == expected

# An empty graph properly returns null
def test_empty_graph():
    graph = Graph()
    actual = graph.size()
    expected = 'null'
    assert actual == expected

@pytest.fixture
def graph():
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

    return graph