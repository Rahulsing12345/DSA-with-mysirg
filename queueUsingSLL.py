class Node:
    def __init__(self,item=None,Next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    
    def is_empty(self):
        return self.front == None   
        # or  self.item_count = 0 then queue is also empty
    
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            #self.rear=n
        else:
            self.rear.next=n
            #self.rear= n
        self.rear=n      #this step is in both if and else block so we can write it outside the conditional statement
        self.item_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        elif self.front == self.rear:   # This condition checks single element in Queue
            self.front = None
            self.rear=None
        else: 
            self.front = self.front.next
        self.item_count -= 1
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.rear.item
    
    def size(self):
        return self.item_count

q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(50)
q1.enqueue(70)
q1.enqueue(90)
print("Front Element",q1.get_front())
print("Rear Element",q1.get_rear())
q1.dequeue()
q1.dequeue()
q1.dequeue()


print("Front Element",q1.get_front())
print("Rear Element",q1.get_rear())
print(q1.is_empty())
            

            

         