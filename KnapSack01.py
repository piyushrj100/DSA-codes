'''The 0-1 knapsack problem is the following. A thief robbing a store finds n
items. The ith item is worth vi dollars and weighs wi pounds, where vi and wi are
integers. The thief wants to take as valuable a load as possible, but he can carry at
most W pounds in his knapsack, for some integer W . Which items should he take?
(We call this the 0-1 knapsack problem because for each item, the thief must either 
take it or leave it behind; he cannot take a fractional amount of an item or take an
item more than once.)


0/1 Knapsack using Dynamic Programming
Time complexity :  O(N*W) or O(num*capacity)

'''

def knapsack (capacity,num,val,weight) :
    dp =[[0 for i in range(capacity+1)] for j in range (num+1)]

    for i in range (1,num+1):
        for w in range (1,capacity+1) :
            
            #if weight of ith item is less than current capacity then, return the max when 
            # ith item is included and 
            #ith item is not included

            if weight[i-1] <=w :
                dp[i][w]=max (dp[i-1][w], val[i-1] + dp[i-1][w-weight[i-1]] )

                # If the weight of ith item is greater than current capacity, 
                # then do not include it 
            
            else :
                dp[i][w]=dp[i-1][w] 

    return dp[num][capacity]

if __name__=='__main__' :
    capacity=50
    weight=[10,20,30]
    val=[60,100,120]
    
    result=knapsack(capacity,len(val),val,weight)
    print("Maximum total profit :", result)


