
'''
# pseudocode from clrs book
MST-KRUSKAL(G, W )
A=φ
2 for each vertex v E V[G]
3   do MAKE-SET(V)
4 sort the edges of E into nondecreasing order by weight w
5 for each edge (u, v) 	ε E, taken in nondecreasing order by weight
6   do if FIND-SET(u) != FIND-SET(v) 
7       then A=A U {(u,v)}
8 UNION(u,v)
9 return A

####Running Time##########

The running time of Kruskal's algorithm for a graph G = (V, E) depends
on the implementation of the disjoint-set data structure. We shall assume the
disjoint-set-forest implementation of Section 21.3 with the union-by-rank and
path-compression heuristics, since it is the asymptotically fastest implementation
known. Initializing the set A in line 1 takes O(1) time, and the time to sort the
edges in line 4 is O (E lg E). (We will account for the cost of the |V| MAKE-SET
operations in the for loop of lines 2-3 in a moment.) The for loop of lines 5-8
performs O (E) FIND-SET and UNION operations on the disjoint-set forest. Along
with the |V|  MAKE-SET operations, these take a total of O((V + E) α(V)) time,
where α is the very slowly growing function defined in Section 21.4. Because G is
assumed to be connected, we have |E| >= |V| - 1, and so the disjoint-set operations
take 0 (E α(V)) time. Moreover, since α( (V I) = O (lg V) = O(lg E), the total
running time of Kruskal's algorithm is O(E 1gE). Observing that |E| < |V|^2,
we have lg |E| = O(lg V), and so we can restate the running time of Kruskal’s
algorithm as O(E lg V). 

'''


class Edge :
    def __init__(self,src,dest,weight) :
        self.src=src
        self.dest=dest
        self.weight=weight

class Graph_MST :
    def __init__(self,vertex) :
        self.vertex=vertex
        self.parent=[-1]*self.vertex
        self.rank=[-1]*self.vertex
        self.EdgeList=[]
    
    def addEdge(self,src,dest,weight) :
        self.EdgeList.append(Edge(src,dest,weight))
    
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
    
    def Kruskal (self) : 
        A=[]
        self.Make_set()
        # sorted_edges=sorted(self.EdgeList, key=lambda u:u.weight)
        self.EdgeList.sort(key=lambda u:u.weight)
        for edge in self.EdgeList :
            if self.find_set(edge.src) != self.find_set(edge.dest) :
                A.append(edge)
                self.union(edge.src,edge.dest)
        return A
    
    def print_mst(self,edges) :
        mst_weight=0
        print("\n++printing MST++\n")
        print("u -- v = weight")
        print("---------------")
        for edge in edges :
            print(edge.src,'--',edge.dest,'=',edge.weight)
            mst_weight+=edge.weight
        print("Weight of the MST: ", mst_weight)

if __name__=='__main__' :
    vertex=9
    graph_mst=Graph_MST(9)

    '''
    Below  graph is being considered, CLRS book , page 632

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
    graph_mst.addEdge(0,1,4)
    graph_mst.addEdge(0,7,8)
    graph_mst.addEdge(1,2,8)
    graph_mst.addEdge(1,7,11)
    graph_mst.addEdge(2,3,7)
    graph_mst.addEdge(2,8,2)
    graph_mst.addEdge(2,5,4)
    graph_mst.addEdge(3,4,9)
    graph_mst.addEdge(3,5,14)
    graph_mst.addEdge(4,5,10)
    graph_mst.addEdge(5,6,2)
    graph_mst.addEdge(6,7,1)
    graph_mst.addEdge(6,8,6)
    graph_mst.addEdge(7,8,7)
    kruskal=graph_mst.Kruskal()
    graph_mst.print_mst(kruskal)





        


    

        







