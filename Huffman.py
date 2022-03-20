#Total running time O(nlgn) with the heap implemetation 
#Huffman Codes compress data very effectively, saving 20 to 90 percent.


from math import inf 

class Node : 
    def __init__(self,char='',freq=None) :
        self.left=None
        self.right=None
        self.freq=freq
        self.char=char
        self.dir='' #direction here means, if the node is left or right of parent. 0 means left and 1 means right


class priority_queue : 
    def __init__(self,array) :
        self.array=array
        self.maxsize=len(self.array)
    
    def parent(self,index) :
        return (index-1)//2

    def left(self,index) :
        return 2*index+1

    def right(self,index):
        return 2*index+2 
    

    def min_heapify(self,index):
        l=self.left(index)
        r=self.right(index)

        if l<self.maxsize and self.array[l].freq< self.array[index].freq :
            smallest=l
        else: 
            smallest=index
        
        if r<self.maxsize and self.array[r].freq<self.array[smallest].freq :
            smallest=r
        
        if smallest != index :
            temp=self.array[index]
            self.array[index]=self.array[smallest] 
            self.array[smallest]=temp
            self.min_heapify(smallest)
    
    def build_min_heap(self) :
        length=self.maxsize//2
        for idx in reversed(range(length)) :
            self.min_heapify(idx) 
    
    def decrease_key(self,index,val) :

        if val>self.array[index].freq : 
            print("Existing key smaller than desired one! Cant perform the operation")
            return
        if index>self.maxsize :
            print("Index out of bound!")
            return 
        self.array[index].freq=val

        while index>0 and self.array[self.parent(index)].freq>self.array[index].freq :
            temp=self.array[index] 
            self.array[index]=self.array[self.parent(index)]
            self.array[self.parent(index)]=temp
            index=self.parent(index)
    
    def extract_min(self) :
        min_node=self.array[0]
        self.array[0]=self.array[self.maxsize-1] 
        self.array.pop(self.maxsize-1)
        self.maxsize=len(self.array)
        self.min_heapify(0)
        return min_node
    

    def insert(self,new_node,val) :
        new_node.freq=inf
        self.array.append(new_node)
        self.maxsize=len(self.array)
        self.decrease_key(self.maxsize-1,val)
    

class huffman_code : 
    def __init__(self,nodes) :
        self.nodes=nodes 
            
        
    def huffman(self) : 
        n=len(self.nodes)
        Q=priority_queue(self.nodes)

        for i in range(n-1) :
            new_node=Node()
            x=Q.extract_min()
            y=Q.extract_min()
            new_node.left=x
            new_node.right=y
            new_node.left.dir=0 #assigning direction to the new nodes added 
            new_node.right.dir=1
            new_node.freq=x.freq+y.freq
            Q.insert(new_node,new_node.freq)
        return Q.extract_min() #Returns the root of the tree 
    
    def print_code(self,root,code='') :
        
        new_code=code+str(root.dir)
        if root.left :
            self.print_code(root.left,new_code)
        if root.right:
            code=code+str(1)
            self.print_code(root.right,new_code)
        
        if root.left is None and root.right is None :
            print(str(root.char)+ "    :    "+str(root.freq)+ "     ==>     " + new_code)


if __name__=='__main__' :
    
    n1=Node('f',5)
    n2=Node('e',9)
    n3=Node('c',12)
    n4=Node('b',13)
    n5=Node('d',16)
    n6=Node('a',45)

    nodes=[n1,n2,n3,n4,n5,n6] 
    h=priority_queue(nodes)
    huff=huffman_code(nodes)
    
    print("Char : Frequency ==> Encoding " )
    print("------------------------------")
    root=huff.huffman()
    huff.print_code(root)