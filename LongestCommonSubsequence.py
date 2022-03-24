'''
Optimal Substructure of an LCS 
Let X=<x1,x2....xm> and Y=<y1,y2,...ym> be sequences. Let Z=<z1,z2,..zk> be any LCS of X and Y.

If xm =yn then zk =xm=yn and Z(k-1) is an LCA of X(m-1) and Y(m-1)
IF xm != yn then zk !=xm implies that Z is an LCA of X(m-1) and Y
If xm != yn, then zk != yn implies that Z  is an LCS of  X and Y(n-1)

c[i][j]= 0 if i=0 or j=0
c[i][j] =c[i-1][j-1] +1
c[i][j]=max(c[i][j-1],c[i-1][j])

Time complexity =O(n^2)

'''

class LCS :
    def lcs_length(self,X,Y) :
        m=len(X)
        n=len(Y)

        b=[[None for i in range(n+1)] for j in range(m+1)] 
        c=[[None for i in range(n+1)] for j in range(m+1)]

        for i in range(1,m+1) :
            c[i][0]=0
        for j in range(n+1) :
            c[0][j]=0 
        for i in range(1,m+1) :
                for j in range(1,n+1) :
                    if X[i-1]==Y[j-1] :
                        c[i][j]=c[i-1][j-1]+1
                        b[i][j]='\\'

                    elif c[i-1][j]>=c[i][j-1] :
                        c[i][j]=c[i-1][j]
                        b[i][j]="|"
                    
                    else :
                        c[i][j]=c[i][j-1]
                        b[i][j]="--"
    
        return c,b

    def print_lcs(self,b,X,i,j) :
        if i==0  or j==0 :
            return
        if b[i][j] == '\\' : 
            self.print_lcs(b,X,i-1,j-1)
            print(X[i-1],end="")
         
        elif b[i][j]=='|' :
            self.print_lcs(b,X,i-1,j)
        
        else :
            self.print_lcs(b,X,i,j-1)


if __name__=='__main__' :
    X="ABCBDAB"
    Y="BDCABA"

    lcs=LCS()
    c,b=lcs.lcs_length(X,Y)
    print("Length of longest common subsequence: ", c[len(X)][len(Y)])
    print("Longest common subsequence: ",end="")
    lcs.print_lcs(b,X,len(X),len(Y)) #X is string with greater length










        

