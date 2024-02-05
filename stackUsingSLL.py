class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next 

class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("STACK IS EMPTY")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise self.is_empty()
        
    def size(self):
        return self.item_count

s3=Stack()
s3.push(10)
s3.push(15)
s3.push(17)
s3.push(21)
print("total element in the stack:",s3.size())
print("top element of Stack",s3.peek())
print("popped element is:",s3.pop())
print("top element of Stack",s3.peek())

            
