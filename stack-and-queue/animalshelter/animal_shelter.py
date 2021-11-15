from stack_and_queue.queue import Queue
class  AnimalShelter:
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()

    def enqueue(self,name,animal):
        if animal.lower() =='cat':
            return self.cat.enqueue(name)

        elif animal.lower() =='dog':
            return self.dog.enqueue(name)

        else:
            return None


    def dequeue (self,pref=None):
        if pref == None:
            raise Exception ("please enter your animal's preference dog or cat")
        elif pref.lower() == 'dog':
            return "dog called "+self.dog.dequeue()+' adopted'
       
        else:
               return 'cat called '+self.cat.dequeue()+' adopted'


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('cat1', 'cat')
    shelter.enqueue('cat2', 'cat')
    print (shelter.dequeue('cat'))
    print (shelter.dequeue('cat'))
    shelter.enqueue('cat3', 'cat')
    shelter.enqueue('dog1', 'dog')
    print (shelter.dequeue('dog'))
    print (shelter.dequeue('cat'))
    print (shelter.dequeue())