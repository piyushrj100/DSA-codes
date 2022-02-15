class Node :  #Creates a new node
    def __init__(self, data=None, next=None) :
        self.data=data
        self.next=next

class LinkedList : 
    def __init__(self) :
          self.head=None
    
    def print_list (self): #prints the linked list 
        if self.head is None :
            print("Empty linked list")
            return 
        itr=self.head
        llstr=''
        while itr :
            llstr+=str(itr.data) + '-->' if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)

    def length(self) : #Finds the total length of the list
        count=0
        temp=self.head
        while temp.next is not None :
            count+=1
            temp=temp.next
        return count
            
    
    def insert_begin(self,data) : # Insets a node at the beginning of the list
             node=Node(data,self.head)
             self.head=node
    
    def insert_end(self,data) : #Inserts a new node at the end of the linked list 
        node=Node(data,self.head)
        if self.head is None :
            self.head=node
            return
        temp=self.head 
        while temp.next :
            temp=temp.next
        temp.next=Node(data,None)

    def del_beg(self) : # Deletes a node at the beginning of the list
        if not self.head :
            print("Nothing to delete")
            return
        temp=self.head
        self.head=self.head.next
        temp=None

    def del_end(self) : #Deletes a list at the end of the list 
        if self.head is None :
            print("Nothing to delete!")
            return
        if self.head.next is None :
            self.head=None
            return
        temp=self.head
        while temp.next.next is not None :
            temp=temp.next
        temp.next=None

    def insert_at_pos(self,pos,data) : #Inserts a node ata given position. Position stats from 1 here
        if pos < 1 or pos>self.length() :
            print("Invalid position!")
            return
        
        if pos ==1 :
            self.insert_begin(data)
            return

        
        temp=self.head
        while temp  :
            pos-=1
            if pos==1 :
                newNode=Node(data,temp.next)
                temp.next=newNode
                break
            temp=temp.next

    def delete_at_pos(self,pos) : # deletes a node from a given position Position starts from 1. 
        if pos <1 or pos > self.length() :
            print("Invalid position. Cannot delete") 
            return 
        if pos==1 :
            self.del_beg()
            return
        temp=self.head
        while  temp.next :
            pos-=1
            if pos==1 :
                temp.next=temp.next.next
                break
            temp=temp.next

            
#Driver code :      
if __name__=='__main__' :
    ll=LinkedList()
    #inserting few elements
    ll.insert_begin(465)
    ll.insert_begin(56)
    ll.insert_end(76)
    ll.insert_end(6)  
    ll.insert_at_pos(3,67)
    ll.insert_at_pos(4,85)
    ll.insert_begin(58)
    ll.insert_end(8)

    ll.print_list()
    
    #delete few elements 
    ll.del_beg()
    ll.delete_at_pos(5)
    ll.del_end()

    ll.print_list() 



