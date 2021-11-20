# ALGORITHM breadthFirst(root)
#  INPUT  <-- root node
#  OUTPUT <-- front node of queue to console

#   Queue breadth <-- new Queue()
#   breadth.enqueue(root)

#   while breadth.peek()
#     node front = breadth.dequeue()
#     OUTPUT <-- front.value

#     for child in front.children
#         breadth.enqueue(child)
class Node:
    def __init__(self, value=None):
        self.value=value
        self.left= None
        self.center= None
        self.right= None

class K_th_Tree:
    output=[]
    def breadthFirst(self,root):
        if root is not None:
            self.output.append(root.value)
            
            def traversal(root):
                if root.left is not None:
                    self.output.append(root.left.value)
                
                if root.center is not None:
                    self.output.append(root.center.value)

                if root.right is not None:
                    self.output.append(root.right.value)
            traversal(root)
            traversal(root.left)
            traversal(root.center)
            traversal(root.right)
            

        return self.output
        

def create_tree():
    tree=K_th_Tree()
    #level 0
    tree.root=Node("A")
    #level 1
    tree.root.left=Node("B")
    tree.root.center=Node("C")
    tree.root.right=Node("D")
    #level 2
    tree.root.left.left=Node("E")
    tree.root.left.center=Node("F")
    tree.root.center.center=Node("G")
    tree.root.right.right=Node("H")
    return tree


if __name__ == '__main__':
    tree = create_tree()
    kth=tree.breadthFirst(tree.root)
    print(kth)

