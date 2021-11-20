from trees.node import Node
class Tree:
    def __init__(self):
        self.root = None
    
    def pre_order(self):
        """
        to iterat tree as root-> left-> right
        """
        output = []
        
        def _traverse(_root = None):
            if _root is None:
                raise Exception('an empty tree')
            output.append(_root.value)
            if _root.left is not None:
                _traverse(_root.left)

            if _root.right is not None:
                _traverse(_root.right)
            

            return output
        return _traverse

    def in_order(self):
        """
        to iterat tree as left-> root-> right
        """
        output = []
        
        def _traverse(_root = None):
            if _root is None:
                raise Exception('an empty tree')
            if _root.left is not None:
                _traverse(_root.left)

            output.append(_root.value)
            if _root.right is not None:
                _traverse(_root.right)
            return output
        return _traverse

    def post_order(self):
        """
        to iterat tree as left-> right-> root
        """
        output = []
        
        def _traverse(_root = None):
            if _root is None:
                raise Exception('an empty tree')

            if _root.left is not None:
                _traverse(_root.left)

            if _root.right is not None:
                _traverse(_root.right)
            output.append(_root.value)
            return output
        return _traverse
            

def create_tree():
    """
        to create tree 
    """
    tree=Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree


if __name__ == "__main__":
    tree = create_tree()
    preOrder= tree.pre_order()
    inOrder = tree.in_order()
    postOrder = tree.post_order()
    print('pre-order: ',preOrder(tree.root))
    print('in-order: ',inOrder(tree.root))
    print('post-order: ',postOrder(tree.root))