class Node : 
    def __init__(self, data=None, next=None) :
        self.data=data
        self.next=next

class LinkedList :
    def __init__(self) :
          self.head=None
    
    def print_list (self):
        if self.head is None :
            print("Empty linked list")
            return 
        itr=self.head
        llstr=''
        while itr :
            llstr+=str(itr.data) + '-->' if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)

    
    def insert_begin(self,data) :
             node=Node(data,self.head)
             self.head=node
    
    def insert_end(self,data) :
        node=Node(data,self.head)
        if self.head is None :
            self.head=node
            return
        temp=self.head 
        while temp.next :
            temp=temp.next
        temp.next=Node(data,None)


             
            
if __name__=='__main__' :
    ll=LinkedList()
    ll.insert_begin(465)
    ll.insert_begin(56)
    ll.insert_end(76)
    ll.insert_end(6)  
    ll.print_list() 



