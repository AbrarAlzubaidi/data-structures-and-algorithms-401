class Node:

    def __init__(self, value):
        self.next=None
        self.value=value


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise Exception("this queue is empty you can't remove from it")
        else:
            temp = self.front
            self.front = temp.next
            temp.next=None

        return temp.value

    def is_empty(self):
        return self.front == None

    def peek(self):
        if self.is_empty():
            raise Exception("this queue is empty you can't remove from it")
        else:
            return self.front.value

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(5)
    queue.enqueue(30)
    print(queue.is_empty())
    print(queue.peek())
    print(queue.dequeue())