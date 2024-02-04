class Stack(list):
    def is_empty(self):
        return len(self)==0

    def push(self,data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return(self[-1])
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return len(self)
    
    def insert(self,index,data):
        raise AttributeError("No Attribute 'insert' in stack")

s2=Stack()
s2.push(10)
s2.push(20)
s2.push(40)
print("TOP OF STACK: ",s2.peek())
s2.pop()
print("TOP OF STACK: ",s2.peek())

        