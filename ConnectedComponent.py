from collections import defaultdict 

class Edge:
    def __init__(self,src,dest) :
        self.src=src
        self.dest=dest


class Graph :    
    def __init__(self,vertex) :
        self.vertex=vertex
        self.parent=[-1]*self.vertex
        self.rank=[-1]*self.vertex
        self.EdgeList=[]
    
    def addEdge(self,src,dest) :
        self.EdgeList.append(Edge(src,dest))
    
    def Make_set (self) :
        for i in range (self.vertex) :
            self.parent[i]=i
            self.rank[i]=0
    def find_set(self,u) :
        if self.parent[u]==u :
            return u
        self.parent[u]=self.find_set(self.parent[u])
        return self.parent[u]

    def union(self,u,v) :
        parent_u=self.find_set(u)
        parent_v=self.find_set(v)
        if parent_u != parent_v :
            if self.rank[parent_u] < self.rank[parent_v] :

                self.parent[parent_u]=parent_v
            elif self.rank[parent_v]<self.rank[parent_u] :
                self.parent[parent_v]=parent_u
            else :
                self.parent[parent_v]=parent_u
                self.rank[parent_u]+=1

    
    def connected_component(self) :
        self.Make_set()
        for edge in self.EdgeList:
            if self.find_set(edge.src) != self.find_set(edge.dest) :
                self.union(edge.src,edge.dest) 
    
    def same_component(self,u,v) :
        self.connected_component()
        if self.find_set(u) == self.find_set(v) :
            return True
        return False
    def count_component(self) :
        self.connected_component()
        count=0
        for i in range(len(self.parent)) :
            if self.parent[i]==i :
                count+=1
        return count
    def print_components(self) :
        d=defaultdict(list) 
        for i in range(self.vertex) :
            x=self.find_set(i)
            d[x].append(i)
        print("The components of the graph are :  ")    
        for value in d.values() : 
            comp="  ".join( str(v) for v in value)
            print(comp)
        

 
 
if __name__=='__main__' :
    vertex=10

    '''
    Below graph is getting created : 

    0-----1     4----5    7    9
    |    /|     |         |
    |  /  |     |         |
    | /   |     |         |
    2     3     6         8   
    

    '''
    graph=Graph(vertex)
    graph.addEdge(0,1)
    graph.addEdge(2,0)
    graph.addEdge(1,2)
    graph.addEdge(1,3)
    graph.addEdge(4,5)
    graph.addEdge(4,6)
    graph.addEdge(7,8)
    # print(graph.EdgeList)  
    graph.connected_component()
    print("Check if the nodes 0 and 9 belong to the same component : ")
    # print(graph.same_component(0,9))
    graph.print_components()
    print("Total number of connected components : ")
    print(graph.count_component())
    
