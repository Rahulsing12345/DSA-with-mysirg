class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
    
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.item_count == 0       # or return self.front == None
    
    def insert_front(self,data):
        n= Node(data,None,self.front)
        if self.is_empty():
            #self.front = n 
            self.rear = n
        else:
            self.front.prev = n
            #self.front = n 
        self.front = n    #this condition is same in bith if-else so we can write it outside the conditional statement 
        self.item_count += 1
    
    def insert_rear(self,data):
        n=Node(data,self.rear,None)
        if self.is_empty():
            self.front = n 
            #self.rear = n
        else:
            self.rear.next = n
            #self.rear = n
        self.rear = n
        self.item_count += 1
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        elif(self.front == self.rear):
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        elif(self.front == self.rear):
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        
        return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        return self.rear.item
    
    def size(self):
        return self.item_count

d1= Deque()
d1.insert_front(11)
d1.insert_front(12)
d1.insert_front(13)
d1.insert_rear(55)
d1.insert_rear(56)
d1.insert_rear(57)
d1.delete_front()

print("Size =",d1.size())
print("Front =", d1.get_front())
print("Rear =",d1.get_rear()) 


    
    



       
