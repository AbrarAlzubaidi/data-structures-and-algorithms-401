from treeBreathFirst.queue import Queue
"""ALGORITHM breadthFirst(root)
// INPUT  <-- root node
// OUTPUT <-- front node of queue to console

  Queue breadth <-- new Queue()
  breadth.enqueue(root)

  while breadth.peek()
    node front = breadth.dequeue()
    OUTPUT <-- front.value

    for child in front.children
        breadth.enqueue(child)"""

class Node():
    
    def __init__(self, value= None):
        self.value= value
        self.children = []

def breadthFirst(root):
    """
    to iterate through k-ary tree with breath first approuch
    """
    output=[]
    queue =Queue()
    
    if root.value is not None:
        queue.enqueue(root)
        while not queue.is_empty():
            f= queue.dequeue()

            if f is not None:
                if f.value % 3==0 and f.value % 5 ==0:
                    output.append("FizzBuzz")
                elif f.value %3 ==0:
                    output.append("Fizz")
                elif f.value %5 ==0:
                    output.append("Buzz")
                else:
                    output.append(str(f.value))
                if f.children !=[]:
                    for child in f.children:
                        queue.enqueue(child)
    else:
        raise Exception('empty tree')
    return output


if __name__ == '__main__':
    root = Node(1)
    root.children.append(Node(2))
    root.children.append(Node(3))
    root.children.append(Node(4)) 
    root.children[0].children.append(Node(5)) 
    root.children[0].children[0].children.append(Node(10)) 
    root.children[0].children.append(Node(6)) 
    root.children[0].children[1].children.append(Node(11))
    root.children[0].children[1].children.append(Node(12))
    root.children[0].children[1].children.append(Node(13)) 
    root.children[2].children.append(Node(15))
    root.children[2].children.append(Node(8))
    root.children[2].children.append(Node(9))
    breath = breadthFirst(root)
    print(breath)
