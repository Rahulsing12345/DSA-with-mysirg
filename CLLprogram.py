class Node:
    def __init__(self,item=None,next=None):
        self.item= item
        self.next= next
class CLL:
    def __init__(self,last=None):
        self.last=last
    
    def is_empty(self):
        if self.last is None:
            return
    
    def insert_at_start(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
    
    def insert_at_last(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
            self.last=new_node
    
    def search(self,data):
        if self.is_empty():
            return None
        else:
            temp=self.last
            if self.last.item==data:
                return self.last
            while temp.next.item != data:
                temp=temp.next
                if self.last==temp:
                    return 
            return temp
            
    def insert_after(self,temp,data):
        if temp is not None:
            if not is_empty():
                new_node=Node(data,temp.next)
                temp.next=new_node
                if temp==self.last:
                    self.last=new_node
                    
    def print_list(self):
        if not is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item, end=' ')
                temp=temp.next
            print(temp.item)
    
    def delete_first(self,):
        if not is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
    
    def delete_last(self,):
        if not is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
                
    def delete_item(self,):
        if not is_empty():
            if self.last.next==self.last:
                if self.last.item== data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:
                    temp=self.last.next
                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                            break
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
cll=CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
cll.print_list()
print()
                
                    
    
    
