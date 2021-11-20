from binary_tree import Tree
from node import Node


class BST(Tree):
    def add(self,_root ,value ):
        node = Node(value)
        if _root is None:
            _root=node     
        else:
            if _root.value<node.value:
                if _root.right is None:
                    _root.right=node
                else:
                    self.add(_root.right,value)
            else:
                if _root.left is None:
                    _root.left = node
                else:
                    self.add(_root.left,value)

    def contains(self, _root,value):
     
        if _root is None or _root.value == value:
            return f"is number {value} is exist ? {True}"

        if _root.value < value:
            if _root.right is None:
                return f"is number {value} is exist ? {False}"
            return self.contains(_root.right,value)

        if _root.value > value:
            if _root.left is None:
                return f"is number {value} is exist ? {False}"
            return self.contains(_root.left,value)


            
        
def create_tree():
    tree=Tree()
    tree.root=Node(23)
    tree.root.left=Node(8)
    tree.root.right=Node(42)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(16)
    tree.root.right.left=Node(27)
    return tree

if __name__ == '__main__':
    tree= create_tree()
    preOrder = tree.pre_order()
    print('before insetrion',preOrder(tree.root))
    bst= BST()
    inser_to_tree = bst.add( tree.root,85)
    preOrder = tree.pre_order()
    print('after insetrion',preOrder(tree.root))
    contain=bst.contains(tree.root,85)
    print(contain)
    