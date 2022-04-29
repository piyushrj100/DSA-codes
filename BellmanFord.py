# Bellman Ford algorithm solves the single source shortest paths problem in the general case where 
# edge weights may be negative.Bellman ford algorithm returns a boolean value indicating whether
# or not there is such a negative cycle reachable from the source. If such cycle exists, 
# there is no such solution.
# Bellman Ford algorithm runs in O(VE)

from math import inf 
class Vertex : 
    def __init__(self) :
        self.adj=[]
        self.pred=None
        self.weight=[]
        self.depth=None
        self.id=None

    def __eq__(self,other) :
        return self.id==other.id
    

class Graph : 
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
    
    def BellmanFord(self,start) :
        self.initialize_single_source(start)
        
        for i in range(len(self.vertices)-1) :
            for u in self.vertices :
                for v,w in zip(u.adj,u.weight) :
                    self.relax(u.id,v,w)
        
        for u in self.vertices :
            for v,w in zip (u.adj,u.weight) :
                if self.vertices[v].depth>u.depth+w :
                    return False 
        return True
    
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
    Bellman=Graph(vertices)
    start=v0
    res=Bellman.BellmanFord(start)
    if (res is True) : 
        print("Shortest Paths exists :")
        Bellman.print_shortest_path(start)

    else :
        print("No solution exists!. Negative cycle exists")