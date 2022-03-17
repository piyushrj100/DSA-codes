
from math import inf 
class Min_heap :
    def __init__(self,array) :
        self.array=array
        self.maxsize=len(self.array)
    
    def parent(self,index) : 
        return (index-1)//2 #index starts from 0

    def left(self,index) :
        return (2*index) +1

    def right(self,index) :
        return (2*index) +2
    
    def Min_Heapify (self, index) :
        l=self.left(index)
        r=self.right(index)

        if l<self.maxsize and self.array[l]<self.array[index] :
            smallest=l
        else :
            smallest=index
        if r<self.maxsize and self.array[r]<self.array[smallest] :
            smallest=r
        
        if smallest != index : 
            temp=self.array[index]
            self.array[index] =self.array[smallest]
            self.array[smallest]=temp  
            self.Min_Heapify(smallest)
        
    def Build_min_heap(self) :
        length=self.maxsize//2
        for idx in reversed(range(length)) :
            self.Min_Heapify(idx)
    
    def Extract_min(self) : #takes logn time 
        if self.maxsize==0 :
            print("Heap is empty! unable to perform operation")
            return inf
        min_el=self.array[0]
        self.array[0]=self.array[self.maxsize-1]
        self.array.pop(self.maxsize-1)
        self.maxsize=len(self.array)
        self.Min_Heapify(0)
        return min_el
    
    def decrease_key(self,index,key) :
        if index>self.maxsize :
            print("Index out of bounds!Unable to perform operation ")
            return inf 
        if self.array[index]<key :
            print("Value is smaller than they current key! Unable to perfirm operation!")
            return inf
        self.array[index]=key
        while index>0 and self.array[self.parent(index)] >self.array[index] :
            temp=self.array[index]
            self.array[index]=self.array[self.parent(index)]
            self.array[self.parent(index)]=temp
            index=self.parent(index)
    
    def insert_key(self,key) :
        self.array.append(inf)
        self.maxsize=len(self.array)
        self.decrease_key(self.maxsize-1,key)
    
if __name__=='__main__' : 
    array=[4,1,3,2,16,9,10,14,8,7]
    print("Array before Heap operations: ")
    print(array) 
    heap=Min_heap(array)
    heap.Build_min_heap()
    print("Min Heap created :")
    print(heap.array)
    print("Extractng minimum element")
    print (heap.Extract_min())
    print("Heap after extract min operation : ")
    print(heap.array)
    print("Inserting an element : ")
    heap.insert_key(0)
    print("Heap after insert key operation:")
    print(heap.array)
    print("Performing decrease key operartion on ")
    heap.decrease_key(4,-8)
    print("Heap after decrease key operation : ")
    print(heap.array)
