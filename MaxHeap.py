import sys
class Binary_heap :
    def __init__(self,array) :
        self.array=array
        self.maxsize=len(self.array)
    
    def parent(self,index) : 
        return (index-1)//2 #index starts from 0
    def left(self,index) :
        return (2*index) +1
    def right(self,index) :
        return (2*index) +2
    

    
    def Max_Heapify (self,index) : 
        l=self.left(index) 
        r=self.right(index)

        if l<self.maxsize and self.array[l] >self.array[index] :
            largest=l
        else :
            largest=index
        if r<self.maxsize and self.array[r]>self.array[largest] :
            largest=r
        if largest != index :
            temp=self.array[index]
            self.array[index] =self.array[largest]
            self.array[largest]=temp  
            self.Max_Heapify(largest)
        
    def Build_max_heap(self) :
        length=self.maxsize//2
        # print(self.maxsize)
        for idx in reversed(range (0,length)) :
            self.Max_Heapify(idx)
    
    def Extract_max(self) : #O(lgn)
        if self.maxsize ==0 :
            print("Heap undeflow!Cannot extract anything")
            return
        max_el=self.array[0]
        self.array[0]=self.array[self.maxsize-1]
        self.array.pop(self.maxsize-1)
        self.maxsize=len(self.array)
        # self.maxsize=self.maxsize-1
        self.Max_Heapify(0)

    def Increase_key(self,index,key) : #O(logn)
        if key<self.array[index] :
            print("Error! Key is smaller than current key")
            return
        self.array[index]=key
        while index>0 and self.array[self.parent(index)] <self.array[index] :
            temp=self.array[index]
            self.array[index]=self.array[self.parent(index)]
            self.array[self.parent(index)]=temp
            index=self.parent(index)

    def Insert(self,key) : #O(logn)
        self.array.append(-sys.maxsize-1)
        self.maxsize=len(array)
        self.Increase_key(self.maxsize-1,key)
            
            
if __name__=='__main__'  :
    array=[4,1,3,2,16,9,10,14,8,7]
    heap=Binary_heap(array)
    heap.Build_max_heap()
    print(heap.array)
    heap.Extract_max()
    # print(heap.array[0:heap.maxsize])
    print(heap.array)
    heap.Increase_key(4,87)
    print(heap.array)
    heap.Insert(16)
    print(heap.array)

 


