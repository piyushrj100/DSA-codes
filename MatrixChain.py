#Time complexity : O(n^3)

from math import inf

class MatrixChain : 
    
    def matrix_chain_order(self,p) :
        n=len(p)-1
        m=[[0 for i in range(n+1)] for j in range(n+1)] 
        s=[[0 for i in range(n+1)] for j in range(n)]
        
        for i in range(1,n+1) :
            m[i][i]=0
        for l in range(2,n+1) :
            for i in range(1,n+1-l+1) :
                j=i+l-1
                m[i][j]=inf
                for k in range(i,j) :
                    q=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                    if q<m[i][j] :
                        m[i][j]=q
                        s[i][j]=k
        return m,s
    
    def print_optimal_parens(self,s,i,j) :
        if i==j:
            print("A"+str(i),"",end="")
            return
        else :
            print("(",end="")
        self.print_optimal_parens(s,i,s[i][j])
        self.print_optimal_parens(s,s[i][j]+1,j)
        print(")",end="")

if __name__=='__main__' :
    mcm=MatrixChain()
    p=[30,35,15,5,10,20,25]

    m,s=mcm.matrix_chain_order(p)
    print("Minimum cost to multiply : ", m[1][len(p)-1])
    print()
    print("Matrix parenthisation: ","",end="")
    mcm.print_optimal_parens(s,1,len(p)-1)




 

    



