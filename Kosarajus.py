
#Time complexity O(V+E)

from math import inf 
class Vertex :
    def __init__(self) :
        self.color='white' 
        self.adj=[]
        self.id=None
        self.pred=None
        self.discover=None
        self.finish=None

class Graph : 
    def __init__(self,vertices) :
        self.vertices=vertices
        for idx,vertex in enumerate(self.vertices) :
            vertex.id=idx
        self.time=None
        self.time=0
        self.stack=[]
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
        self.stack.append(u)
        print('v'+str(u.id)+" ", end="")
    
    def dfs(self) :
        # for vertex in self.vertices :
        #     vertex.color='white' 
        #     vertex.pred=None
        # self.time=0

        for vertex in self.vertices :
            if vertex.color=='white' :
                self.dfs_visit(vertex)
    
    def transpose(self) : 
        vertex_list=[]
        for idx in range(len(self.vertices)) :
            # globals()[f"t{idx}"]=Vertex()
            # vertex_list.append(globals()[f"t{idx}"])
            vertex_list.append(Vertex())

        for idx in range(len(self.vertices)) :

            for i in self.vertices[idx].adj :
                vertex_list[i].adj.append(idx)
            
        return Graph(vertex_list)
    
    def SCC(self) :
        count=0
        print("DFS vertex ordered according to their finish time : ")
        self.dfs()
        print("")
        stack = sorted(self.vertices, key=lambda u:u.finish)
        t_graph=self.transpose()
        
        # for vertex in t_graph.vertices :
        #     vertex.color='white' 
        #     vertex.pred=None
        # t_graph.time=0 
        print("The Connected components are : ")
        while stack :
            ins=stack.pop()
            if t_graph.vertices[ins.id].color=='white' :
                t_graph.dfs_visit(t_graph.vertices[ins.id])
                print()
                count+=1
        print("Total connected components : ", count)


    

if __name__=='__main__' :
    
    #Both the graphs are from CLRS book
    print("Finding strongly connected components for first graph.....\n")
    v0=Vertex()
    v1=Vertex()
    v2=Vertex()
    v3=Vertex()
    v4=Vertex()
    v5=Vertex()
    v6=Vertex()
    v7=Vertex()


    v0.adj=[1]
    v1.adj=[2,4,5]
    v2.adj=[3,6]
    v3.adj=[2,7]
    v4.adj=[0]
    v5.adj=[6]
    v6.adj=[5,7]
    v7.adj=[7]
    vertices=[v0,v1,v2,v3,v4,v5,v6,v7] 
    graph=Graph(vertices)
    graph.SCC()

    print("\n\n")

    print("Finding strongly connected components for second graph.....\n")
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

    vertices_1=[v0,v1,v2,v3,v4,v5] 

    graph_1=Graph(vertices_1)
    
    graph_1.SCC()



