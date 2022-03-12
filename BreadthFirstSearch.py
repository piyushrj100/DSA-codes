import queue
from math import inf 
class Vertex :
    def __init__(self) :
        self.color=None
        self.depth=None
        self.adj=[]
        self.pred=None
        self.id=None
    

class Graph :
    def __init__(self,vertices) :
        self.vertices=vertices
        for idx,vertex in enumerate(self.vertices) :
            vertex.id=idx
        self.start=None
    
    def BFS(self,start) :
        self.start=start

        for vertex in self.vertices :
            if vertex.id==self.start.id:
                continue
            vertex.color='white'
            vertex.depth=inf
            # vertex.pred=None
        self.start.color='gray'
        # start.pred=None
        self.start.depth=0
        q=queue.Queue()
        q.put(self.start)
        while (not q.empty()) :
            u=q.get()
            # print( "v"+str(u.id)," ", end="")
            for v in u.adj :
                if self.vertices[v].color=='white' :
                    self.vertices[v].color='gray'
                    self.vertices[v].depth=u.depth+1
                    self.vertices[v].pred=u
                    q.put(self.vertices[v])
            u.color='black'

    def Print_Path(self,v) :
        if self.start.id==v.id :
            print("v"+str(self.start.id)," ",end="")
        elif v.pred==None :
            print("\nNo path exists from start to vertex v")
        else :
            self.Print_Path(v.pred)
            print("v"+str(v.id)," ",end="")


if __name__=='__main__':

    v0=Vertex()
    v1=Vertex()
    v2=Vertex()
    v3=Vertex()
    v4=Vertex()
    v5=Vertex()
    v6=Vertex()
    v7=Vertex()
    
    v0.adj=[1,4]
    v1.adj=[0,5]
    v2.adj=[3,5,6]
    v3.adj=[2,6,7]
    v4.adj=[0]
    v5.adj=[1,2,6]
    v6.adj=[2,3,5,7]
    v7.adj=[3,6]
    graph=Graph(vertices=[v0,v1,v2,v3,v4,v5,v6,v7])
    print("Applying BFS...")
    graph.BFS(start=v1)
    print("\n")
    print("Printing the path from start to  vertex  v6:")
    graph.Print_Path(v6)







