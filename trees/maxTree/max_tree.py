from trees.node import Node
from trees.binary_tree import Tree

def create_tree():
    tree = Tree()
    #level 0
    tree.root = Node(40)
    #level 1
    tree.root.left = Node(10)
    tree.root.right = Node(11)
    #level 2
    tree.root.left.left = Node(78)
    tree.root.left.right = Node(46)
    tree.root.right.right = Node(9)
    return tree

if __name__ == '__main__':
    tree = create_tree()
    max= tree.get_max(tree.root)
    print('max of tree: ',max)
