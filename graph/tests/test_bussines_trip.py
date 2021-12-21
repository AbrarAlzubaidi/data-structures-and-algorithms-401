from graph.bussiness_trip import business_trip
from graph.graph import Graph
import pytest

path1=['Metroville', 'Pandora' ]
path2= ['Arendelle', 'Monstroplolis', 'Naboo' ]
path3= ['Naboo', 'Pandora']
path4= ['Narnia', 'Arendelle', 'Naboo']

def test_bussiness_trip(graph2):
    actual1 = business_trip(graph2, path1)
    expected1 = 'True, $82'
    assert actual1 == expected1

    actual2 = business_trip(graph2, path2)
    expected2 = 'True, $115' 
    assert actual2 == expected2

    actual3 = business_trip(graph2, path3)
    expected3 = 'False, $0'
    assert actual3 == expected3

def test_empty_path(graph2):
    actual = business_trip(graph2)
    expected = 'enter a path'
    assert actual == expected

def test_empty_graph():
    g = Graph()
    actual = business_trip(g, path1)
    expected = 'empty graph'
    assert actual == expected

@pytest.fixture
def graph2():
    graph = Graph()
    node1=graph.add_node('Pandora')
    node2=graph.add_node('Arendelle')
    node3=graph.add_node('Metroville')
    node4=graph.add_node('Monstroplolis')
    node5=graph.add_node('Narnia')
    node6=graph.add_node('Naboo')
    # node1 : node2,3
    graph.add_edge(node1, node2, 150)
    graph.add_edge(node1, node3, 82)

    # node2: node1,3,4
    graph.add_edge(node2, node1, 150)
    graph.add_edge(node2, node3, 99)
    graph.add_edge(node2, node4, 42)

    # node3 : node1,2,4,5,6
    graph.add_edge(node3, node1, 82)
    graph.add_edge(node3, node2, 99)
    graph.add_edge(node3, node4, 105)
    graph.add_edge(node3, node5, 37)
    graph.add_edge(node3, node6, 26)

    # node4 : node2,3,6
    graph.add_edge(node4, node2, 42)
    graph.add_edge(node4, node3, 105)
    graph.add_edge(node4, node6, 73)

    # node5 : node3,6
    graph.add_edge(node5, node3, 37)
    graph.add_edge(node5, node6, 250)

    # node6 : node3,4,5
    graph.add_edge(node6, node3, 26)
    graph.add_edge(node6, node4, 73)
    graph.add_edge(node6, node5, 250)

    return graph 