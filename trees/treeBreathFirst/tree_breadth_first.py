from trees.binary_tree import Tree
from queue import Queue

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


def breadthFirst(root):
  """
  search through a tree one level at a time  
  """
  output=[]
  queue = Queue()
  if root is not None:
    queue.enqueue(root)
    
    while not queue.is_empty():
      f= queue.dequeue()
      if f is not None:
        output.append(f.value)

        if root.left is not None:
          queue.enqueue(f.left)

        if root.right is not None:
          queue.enqueue(f.right)

  return output

            
def create_tree():
    tree = Tree()
    #level 0
    tree.root = Node(2)
    #level 1
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    #level 2
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.right.right = Node(9)
    #level 3
    tree.root.left.right.right = Node(11)
    tree.root.left.right.left = Node(5)
    tree.root.right.right.left = Node(4)
    return tree

if __name__ == '__main__':
  tree = create_tree()
  root =tree.root
  breath=breadthFirst(tree.root)
  inorder= tree.in_order()
  print(breath)

