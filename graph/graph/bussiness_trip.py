from graph.graph import Graph
def business_trip(graph,path=''):
    sum=0
    nodes= list(graph.get_nodes())
    adj_nodes=set()
    if path == '' or path == ' ':
        return 'enter a path'
    if nodes == []:
        return 'empty graph'
    for city in path:
        if city not in nodes:
            raise Exception(f'{city} not found')

    for i in range(len(path)-1):
        for node in nodes:
            if path[i]== node:
                target_node=node
        for edge in graph.get_neighbors(target_node):
            adj_nodes.add(edge[0])
            if edge[0] == path[i+1]:
                # print(adj_nodes)
                # print('edge ',edge[0])
                sum+= edge[1]

        if path[i+1] not in adj_nodes:
            return 	f'False, $0'

    return f'True, ${sum}'  


if __name__ == '__main__':
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
    
    path1=['Metroville', 'Pandora' ]
    path2= ['Arendelle', 'Monstroplolis', 'Naboo' ]
    path3= ['Naboo', 'Pandora']
    path4= ['Narnia', 'Arendelle', 'Naboo']

    print(business_trip(graph,path1))