
class Edge:
    def __init__(self,src,dest) :
        self.src=src
        self.dest=dest


class Graph :    
    def __init__(self,vertex) :
        self.vertex=vertex
        self.make_set=[-1]*self.vertex
        self.EdgeList=[]
    
    def addEdge(self,src,dest) :
        self.EdgeList.append(Edge(src,dest))
    
    def find_set(self,i) :
        while self.make_set[i] != i :
            i=self.make_set[i]
        return i 
    def union(self,u,v) : 
          root_u=self.find_set(u)
          root_v=self.find_set(v)
          self.make_set[root_u]=root_v

    
    def connected_component(self) :
        for i in range(self.vertex) :
            self.make_set[i]=i
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
        for i in range(len(self.make_set)) :
            if self.make_set[i]==i :
                count+=1
        return count

 
if __name__=='__main__' :
    vertex=10

    '''
    Below graph is getting created : 

    0-----1     4----5    7    9
    |    /|     |         |
    |  /  |     |         |
    | /   |     |         |
    2/    3     6         8   
    
    
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
    print("Total number of connected components : ")
    print(graph.count_component())
