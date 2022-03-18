import copy 
from math import inf 

class Vertex : 
    def __init__(self):
        self.adj=[]
        self.weight=[]
        self.key=inf
        self.pred=None
        self.id=None
    
    def __eq__(self,other) :
        return self.id==other.id



class Heap : 
    def __init__(self,arr) :
        self.array=copy.deepcopy(arr)
        self.maxsize=len(self.array)
    
    def parent(self,index):
        return (index-1)//2

    def left(self,index) :
        return (2*index +1)
    
    def right(self,index) :
        return (2*index+2)
    

    def Min_Heapify(self,index) :
        l=self.left(index)
        r=self.right(index)
        if l<self.maxsize and self.array[index].key >self.array[l].key :
            smallest=l
        else :
            smallest=index

        if r<self.maxsize and self.array[smallest].key>self.array[r].key :
            smallest=r
        
        if smallest != index :
            temp=self.array[index]
            self.array[index]=self.array[smallest]
            self.array[smallest]=temp
            self.Min_Heapify(smallest)
    
    def Build_min_heap(self) :
        length=self.maxsize//2
        for idx in reversed(range(length)) :
            self.Min_Heapify(idx)
 

    def extract_min(self) :
        min_node=self.array[0]
        self.array[0]=self.array[self.maxsize-1] 
        self.array.pop(self.maxsize-1)
        self.maxsize=len(self.array)
        self.Min_Heapify(0)
        return min_node

    def decrease_key(self,idx,val) :
        index=None
        for i, ins in enumerate(self.array) :
            if ins.id==idx:
                index=i
        

        if val>self.array[index].key :
            print("Value smaller than the decrease key value! Unable  to perform the operation")
        if self.maxsize<=index :
            print("Wrong index ")
        self.array[index].key=val

        while index>0 and self.array[self.parent(index)].key>self.array[index].key :
            temp=self.array[index]
            self.array[index]=self.array[self.parent(index)]
            self.array[self.parent(index)]=temp
            index=self.parent(index)
    
class Graph_MST :
    def __init__(self,vertices) :
        self.vertices=vertices
        for idx,vertex in enumerate(self.vertices) :
            vertex.id=idx
    

    def mst_prim(self,root) :
        for u in self.vertices :
            u.key=inf 
            u.pred=None 
        root.key=0

        Q=Heap(self.vertices)
        Q.Build_min_heap()
        while Q.maxsize >0 :
            u=Q.extract_min()
            # print(u.key)
            # print(Q.array)
            for v, w in zip(u.adj,u.weight) :
                if self.vertices[v] in Q.array and w<self.vertices[v].key :
                    self.vertices[v].pred=u
                    self.vertices[v].key=w
                    Q.decrease_key(self.vertices[v].id,w)
    
    def print_mst(self,root) :
        count=0
        print("Printing the Edge(u,v) and weight included in mst :\n")
        print('u  -- v  = weight')
        print('-----------------')
        for vertex in self.vertices : 
            if vertex.id==root.id :
                continue 
            print('v'+str(vertex.pred.id)+' -- '+ 'v'+str(vertex.id)+' = '+str(vertex.key))
            count+=vertex.key
        
        print("\n Total weight of MST: ", count)
        print()





if __name__=='__main__' :


    '''
    Below  graph is being considered, CLRS book , page 635

                   8       7    
              (1)------(2)------(3)
        4   / |       /  \       | \ 9
          /   |     / 2    \     |   \
       (0)  11|   (8)       \ 4  |14  (4)
        \     |  /7  \6       \  |    /
       8  \   | /     \         \|  / 10
            (7)-------(6)-------(5)
                  1        2
    
    '''


    

    v0=Vertex()
    v1=Vertex()
    v2=Vertex()
    v3=Vertex()
    v4=Vertex()
    v5=Vertex()
    v6=Vertex()
    v7=Vertex()
    v8=Vertex()

    v0.adj=[1,7]
    v1.adj=[0,2,7]
    v2.adj=[1,3,5,8]
    v3.adj=[2,4,5]
    v4.adj=[3,5]
    v5.adj=[2,3,4,6]
    v6.adj=[5,7,8]
    v7.adj=[0,1,6,8]
    v8.adj=[2,6,7]

    v0.weight=[4,8]
    v1.weight=[4,8,11]
    v2.weight=[8,7,4,2]
    v3.weight=[7,9,14]
    v4.weight=[9,10]
    v5.weight=[4,14,10,2]
    v6.weight=[2,1,6]
    v7.weight=[8,11,1,7]
    v8.weight=[2,6,7]
    vertices=[v0,v1,v2,v3,v4,v5,v6,v7,v8]

    graph_mst=Graph_MST(vertices)
    root=v0
    graph_mst.mst_prim(root)
    graph_mst.print_mst(root)
    
    


    




        






        








