# By modifying the PARTITION procedure, we can design another randomized version of quicksort that uses this random-choice
#  strategy. At each step of the quicksort algorithm, before the array is partitioned, we exchange element A[p] with an 
# element chosen at random from A[p . . r]. This modification ensures that the pivot element x = A[p] is equally likely
#  to be any of the r - p elements in the subarray. Thus, we expect the split of the input array to be reasonably 
# well balanced on average. The randomized algorithm based on randomly permuting the input array also works well on 
# average, but it is somewhat more difficult to analyze than this version.

import random

def Partition(A,p,r) :
    random_num=random.randint(p,r)
    x=A[r]
    i=p-1
    for j in range (p,r) :
        if A[j]<=x :
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def Randomized_Partition(arr,start,end) :
    random_num=random.randint(start,end)
    arr[end],arr[random_num]=arr[random_num],arr[end]   #Swapping the pivot with an element randomly chosen.
    return Partition(arr,start,end)


def Randomized_Quicksort (arr,start,end) :
    if start<end :
        q=Randomized_Partition(arr,start,end)
        Randomized_Quicksort(arr,start,q-1)
        Randomized_Quicksort(arr,q+1,end)
    return arr

array=[56,4,3,11,6,877,4,7,0,-2,-53,11]
arr_len=len(array)
end=arr_len-1
start=0
final_result=Randomized_Quicksort(array,start,end)
print(final_result)
