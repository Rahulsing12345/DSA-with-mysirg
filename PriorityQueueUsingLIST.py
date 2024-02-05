class PriorityQueue:
    def __init__(self):
        self.item = []
    
    def is_empty(self):
        return len(self.item) == 0
    
    def push(self,data,priority):
        index = 0
        '''loop is start when Self.item_count contain some list_items and check Self.item_count's index and.......... 
         .....inside index it check the priority_no. is less aur equal to given priority'''
        
        while (index < len(self.item))  and ((self.item[index][1]) <= (priority)):
            index += 1
        self.item.insert(index,(data,priority))
    
    def pop(self):
        if self.is_empty():
            raise IndexError(" Priority Queue is empty")
        return self.item.pop(0)[0]
    
    def size(self):
        return len(self.item)

p=PriorityQueue()
p.push("Amit", 5)
p.push("Mohit", 2)
p.push("Rohan", 3)
p.push("Shyam", 1)
p.push("gauri", 6)
while not p.is_empty():
    print(p.pop())
        

       

        