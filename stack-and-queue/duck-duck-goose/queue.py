from node import Node

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def enqueue(self,value):
        node = Node(value)

        if self.is_empty():
            print('is empty ',value)
            self.front = node
            self.count+=1
        else:
            print('else ',value)
            self.rear = node
            self.rear = self.front
            self.count+=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("this queue is empty you can't remove from it")
        else:
            temp = self.front
            self.front = temp.next
            self.rear.next=self.front
            temp.next=None
            self.count-=1

        return temp.value

    def is_empty(self):
        return self.front == None

    def peek(self):
        if self.is_empty():
            raise Exception("this queue is empty you can't remove from it")
        else:
            return self.front.value


if __name__ == '__main__':
    qu= Queue()
    qu.enqueue("a")
    qu.enqueue("b")
    qu.enqueue("c")
    qu.enqueue("d")
    qu.enqueue("e")
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())
