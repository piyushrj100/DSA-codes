#Time complexity: O(V+E)

import queue
from math import inf
from time import time 
class Vertex :
    def __init__(self) :
        self.color=None
        self.adj=[]
        self.id=None
        self.pred=None
        self.discover=None
        self.finish=None

class Graph :
    def __init__(self,vertices):
        self.vertices=vertices
        for idx,vertex in enumerate(self.vertices) :
            vertex.id=idx
        self.time=None
    
    def dfs_visit(self,u) :
        self.time+=1
        u.discover=self.time
        u.color='gray'
        
        for v in u.adj :
            if self.vertices[v].color=='white' :
                self.vertices[v].pred=u
                self.dfs_visit(self.vertices[v]) 
        u.color='black'
        self.time+=1
        u.finish=self.time
        print('v'+str(u.id)+'-->',u.finish," ",end="")

    
    def dfs(self) :
        for vertex in self.vertices:
            vertex.color='white'
            vertex.pred=None
        self.time=0

        for vertex in self.vertices :
            if vertex.color=='white' :
                self.dfs_visit(vertex)


if __name__=='__main__' :
    v0=Vertex()
    v1=Vertex()
    v2=Vertex()
    v3=Vertex()
    v4=Vertex()
    v5=Vertex()

    v0.adj=[1,3]
    v1.adj=[4]
    v2.adj=[4,5]
    v3.adj=[1]
    v4.adj=[3]
    v5.adj=[5]

    graph=Graph(vertices=[v0,v1,v2,v3,v4,v5])
    print("Applying DFS and printing the finish time of each vertex: ")
    graph.dfs()


        

        

