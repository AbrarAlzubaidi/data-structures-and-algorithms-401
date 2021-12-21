from graph.breathfirst import Graph

import pytest

def test_depth_first():
    graph = Graph()
    node1=graph.add_node('a')
    node2=graph.add_node('b')
    node3=graph.add_node('c')
    node4=graph.add_node('d')
    node5=graph.add_node('e')
    node6=graph.add_node('f')
    node7=graph.add_node('g')
    node8=graph.add_node('h')
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node4)
    graph.add_edge(node2, node1)
    graph.add_edge(node2, node4)
    graph.add_edge(node2, node3)
    graph.add_edge(node3, node2)
    graph.add_edge(node7, node3)
    graph.add_edge(node4, node1)
    graph.add_edge(node4, node2)
    graph.add_edge(node4, node5)
    graph.add_edge(node4, node6)
    graph.add_edge(node4, node8)
    graph.add_edge(node5, node4)
    graph.add_edge(node6, node4)
    graph.add_edge(node6, node8)
    graph.add_edge(node8, node4)
    graph.add_edge(node8, node6)
    actual=graph.depth_first(node1)
    expected = ['a', 'b', 'd', 'a', 'e', 'f', 'h', 'c']
    assert actual == expected

