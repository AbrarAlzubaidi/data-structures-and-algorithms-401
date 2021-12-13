from tree_intersection.hash_table import HashTable
from tree_intersection.binary_tree import Tree
from tree_intersection.node import Node

def tree_intersection(tree1,tree2):
    intersection=[]
    hashtable=HashTable()

    if tree1.root== None or tree2.root==None:
        raise Exception('An empty tree !!') 

    tree1_data=tree1.pre_order()
    print('tree 1 is: ',tree1_data)
    tree2_data=tree2.pre_order()
    print( 'tree 2 is: ',tree2_data)
    for data1 in tree1_data:
        hashtable.add(str(data1),str(data1))

    for data2 in tree2_data:
        if hashtable.contains(str(data2)):
            intersection.append(data2)
    
    if intersection==[]:
        return 'No intersection between two trees'

    return intersection

if __name__=='__main__':
    tree1=Tree()
    tree1.root=Node("A1")
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

    print(tree_intersection(tree1,tree2))