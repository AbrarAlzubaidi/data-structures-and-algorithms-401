from queue import Queue

def duckDuckGoose(qu,n):
    initial = qu.front
    q=None
    print(not qu.is_empty())
    while qu.count != 1:
        t=initial
        i=1
        print(qu.front.value)
        while i<n:
            q=t
            t=t.next
            i+=1
            
        q.next =t.next
        initial= t.next
        t.next= None
        qu.count-=1
        continue
    return qu.front.value    
        




if __name__ == '__main__':
    qu= Queue()
    qu.enqueue("a")
    qu.enqueue("b")
    qu.enqueue("c")
    qu.enqueue("d")
    qu.enqueue("e")
    qu.rear = qu.front
    duckDuckGoose(qu,1)