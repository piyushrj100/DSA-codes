def CountingSort(arr,k) :
    B=[ 0 for i in range(len(arr))]
    print(B)
    temp=[0]*(k+1)
    for j in range(0,len(arr)) :
        temp[arr[j]]=temp[arr[j]]+1
    #temp[i] now contains the number of elements of elements
    print(temp)
    for i in range(1,k+1) :
        temp[i]=temp[i] +temp[i-1]
    print(temp)
    #temp[i] now contains the number of elements less than or equal to i
    for j in range (0,k+1) :
        temp[j]-=1
    for j in reversed(range(len(arr))) :
        B[temp[arr[j]]] =arr[j]
        
        temp[arr[j]] =temp[arr[j]]-1
    return B

arr=[2,5,3,0,2,3,0,3]
res=CountingSort(arr,5)
print(res)



