class Deque:
    def __init__(self):
        self.item=[]        #initialize empty list
    
    def is_empty(self):
        return len(self.item)==0
    
    def insert_front(self,data):
        self.item.insert(0,data)

    def insert_rear(self,data):
        #self.item.insert(-1,data)
        self.item.append(data)
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            self.item.pop(0)
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            self.item.pop()
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.item[0]
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.item[-1]
    
    def size(self):
        return len(self.item)
    
d1= Deque()
d1.insert_front(11)
d1.insert_front(12)
d1.insert_front(13)
d1.insert_rear(55)
d1.insert_rear(56)
d1.insert_rear(57)
d1.delete_front()
d1.delete_rear()
print("Size =",d1.size())
print("Front =", d1.get_front())
print("Rear =",d1.get_rear()) 
