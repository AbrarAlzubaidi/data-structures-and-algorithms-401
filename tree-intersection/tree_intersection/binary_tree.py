from tree_intersection.node import Node
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
    
    def pre_order(self):
        """ root-left-right """
        self.values=[]
         
        if self.root == None:
            return "Tree is Empty"

        def _traverse(node):
            self.values+=[node.value]
            if node.left:
                _traverse(node.left)
            if node.right:
                _traverse(node.right)
            return self.values
            
        return _traverse(self.root)

          

def create_tree():
    """
        to create tree 
    """
    tree1=Tree()
    tree1.root=Node("A")
    tree1.root.left=Node("B")
    tree1.root.right=Node("C")
    tree1.root.left.left=Node("D")
    tree1.root.left.right=Node("E")
    tree1.root.right.left=Node("F")

    tree2=Tree()
    tree2.root=Node("A")
    tree2.root.left=Node("B")
    tree2.root.right=Node("C")
    tree2.root.left.left=Node("D")
    tree2.root.left.right=Node("E")
    tree2.root.right.left=Node("F")

    return [tree1, tree2]


if __name__ == "__main__":
    tree = create_tree()
    preOrder= tree[0].pre_order()
    print('pre-order: ',preOrder(tree[0].root))

    preOrder =tree[1].pre_order()
    print('pre-order: ',preOrder(tree[1].root))

    
