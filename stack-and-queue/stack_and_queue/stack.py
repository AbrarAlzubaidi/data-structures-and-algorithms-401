from stack_and_queue.node import Node

class Stack:
    def __init__(self):
        self.tos=None

    def push(self,value):
        node = Node(value)
        if self.is_empty():
            self.tos=node
        else:
            node.next=self.tos
            self.tos=node

    def pop(self):

        if self.is_empty():
            raise Exception("This stack is empty you can't remove from it ")
        else:    
            temp = self.tos
            self.tos = temp.next
            temp.next=None
            return temp.value

    def is_empty(self):
        return self.tos == None

    def peek(self):
        if self.is_empty():
            raise Exception("This stack is empty you can't peek")
        else:
            return self.tos.value

if __name__ == '__main__':
    stack =Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    # print(stack.peek())
    # print(stack.pop())