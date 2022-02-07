#Quicksort Algorithm
def Partition(A,p,r) :
    x=A[r]
    i=p-1
    for j in range (p,r): 
        if A[j]<=x :
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return (i+1)

def Quicksort(arr, start, end) :
    if start < end :
        q=Partition(arr,start,end)
        Quicksort(arr,start,q-1)
        Quicksort(arr,q+1,end)
    return arr
array=[56,4,3,11,6,877,4,7,0,-2,-53,11]
arr_len=len(array)
end=arr_len-1
start=0
final=Quicksort(array,start,end)
print(final)
