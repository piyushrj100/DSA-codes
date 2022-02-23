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
    
    def exchange(self,idx_1,idx_2) :
        temp=self.array[idx_1] 
        self.array[idx_1]=self.array[idx_2]
        self.array[idx_2]=temp
        
    def heapsort(self) :
        self.Build_max_heap()
        print(self.maxsize)
        for idx in reversed(range(1,self.maxsize)) :
            self.exchange(0,idx)
            self.maxsize=self.maxsize-1
            self.Max_Heapify(0)

if __name__=='__main__' :
    array=[4,1,3,2,16,9,10,14,8,7]
    heap=Binary_heap(array)
    print(heap.array)
    heap.heapsort()
    print(heap.array)





    
