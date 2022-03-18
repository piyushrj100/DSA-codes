#Single Source shortest path problem
#Running time : O((E+V)lgV)
#Each extract min operation take O(lgV). Total V operations for V vertices
#Each decrease key operation (relax) takes O(lgV) Total E operations.

from math import inf 
import copy 

class Vertex : 
    def __init__(self) :
        self.adj=[]
        self.pred=None
        self.weight=[]
        self.depth=None
        self.id=None

    def __eq__(self,other) :
        return self.id==other.id
    

class Min_priority_queue :
    def __init__(self,arr) :
        self.array=copy.deepcopy(arr)
        self.maxsize=len(self.array) 
     
    def parent(self,index) :
        return (index-1) //2

    def left(self,index) :
        return 2*index +1 

    def right(self,index) :
        return 2*index +2 
    
    def min_heapify(self,index) :
        l=self.left(index)
        r=self.right(index)

        if l<self.maxsize and self.array[l].depth <self.array[index].depth :
            smallest=l
        else :
            smallest=index
        if r<self.maxsize and self.array[r].depth< self.array[smallest].depth :
            smallest=r
        
        if smallest!= index :
            temp=self.array[index] 
            self.array[index]=self.array[smallest] 
            self.array[smallest]=temp
            self.min_heapify(smallest)
    
    def build_min_heap(self) :
        length=self.maxsize//2
        for idx in reversed(range(length)) :
            self.min_heapify(idx)
    
    def extract_min(self) :
        min_node=self.array[0]
        self.array[0]=self.array[self.maxsize-1]
        self.array.pop(self.maxsize-1)
        self.maxsize=len(self.array)
        self.min_heapify(0)
        return min_node
    
    def decrease_key(self,idx,val) :
        index=None
        for i, ins in enumerate(self.array) :
            if ins.id==idx:
                index=i
 
        if val>self.array[index].depth :
                print("Value greater than the decrease key value! Unable  to perform the operation")
        if self.maxsize<=index :
            print("Wrong index ")
        self.array[index].depth=val

        while index>0 and self.array[self.parent(index)].depth>self.array[index].depth :
            temp=self.array[index]
            self.array[index]=self.array[self.parent(index)]
            self.array[self.parent(index)]=temp
            index=self.parent(index)

    
class Graph_Dijkstra :
    def __init__(self,vertices) :
        self.vertices=vertices 

        for idx,vertex in enumerate(self.vertices) :
            vertex.id=idx
    
    def initialize_single_source(self,start) :
        for vertex in self.vertices :
            vertex.depth=inf
            start.depth=0

    def relax(self,u,v,w) :
        if self.vertices[v].depth>self.vertices[u].depth + w:
            self.vertices[v].depth=self.vertices[u].depth + w
            self.vertices[v].pred=self.vertices[u]
        
        
    def Dijkstra(self,start) :
        self.initialize_single_source(start) 
        S=[]
        Q=Min_priority_queue(self.vertices) 
        Q.build_min_heap()
        while Q.maxsize >0 :
            u=Q.extract_min()
            S.append(u)
            for v,w in zip(u.adj,u.weight) :
                if self.vertices[v] in S :
                    continue
                self.relax(u.id,v,w)
                Q.decrease_key(self.vertices[v].id,self.vertices[v].depth )
    
    def print_shortest_path(self,start) :
        print("Printing shortest path distance from v"+str(start.id)+" to other nodes :\n")
        print("src      dest  distance")
        print('-----------------------')
        for vertex in self.vertices :
            print('v'+str(start.id)+' -->--> '+'v'+str(vertex.id)+' ==> '+str(vertex.depth))
        print()

        

if __name__=='__main__' :
    v0=Vertex()
    v1=Vertex()
    v2=Vertex()
    v3=Vertex()
    v4=Vertex()

    v0.adj=[1,3]
    v1.adj=[2,3]
    v2.adj=[4]
    v3.adj=[1,2,4]
    v4.adj=[0,2]

    v0.weight=[10,5]
    v1.weight=[1,2]
    v2.weight=[4]
    v3.weight=[3,9,2]
    v4.weight=[7,6]
    vertices=[v0,v1,v2,v3,v4]
    dijkstra=Graph_Dijkstra(vertices)
    start=v0
    dijkstra.Dijkstra(start)
    dijkstra.print_shortest_path(start)

    