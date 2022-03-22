#Running time : O(n^3)

from math import inf 
class FloydWarshall :
	def __init__(self,graph) :
		self.graph=graph
	
	def floyd_warshall (self):
		D=[]
		n=len(self.graph)
		D=[[[ None for i in range(n)] for j in range(n)] for k in range(n+1)]
		D[0]=self.graph
		for k in range(1,n+1) :
			for i in range(n) :
				for j in range(n) :
					D[k][i][j]=(min(D[k-1][i][j],D[k-1][i][k-1]+D[k-1][k-1][j]))
		return D[n]

if __name__=='__main__' :
	graph=[[0,3,8,inf,-4],
	[inf,0,inf,1,7],
	[inf,4,0,inf,inf],
	[2,inf,-5,0,inf],[inf,inf,inf,6,0]
	]

	floyd=FloydWarshall(graph)
	res=floyd.floyd_warshall()
	print(res)

		