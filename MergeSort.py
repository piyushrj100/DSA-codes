from math import inf

def Merge(array,start,mid,end) :
    n1=mid-start+1
    n2=end-mid
    L1=[0]*(n1+1)
    L2=[0]*(n2+1)
    for i in range(0,n1) :
        L1[i]=array[start+i]
    for j in range(0,n2) :
        L2[j]=array[mid+j+1]
    L1[n1]=inf
    L2[n2]=inf
    i=0
    j=0
    for k in range(start,end+1) :
        if L1[i]<=L2[j] :
            array[k]=L1[i]
            i+=1
        else :
            array[k]=L2[j]
            j+=1



def Merge_sort(array,start,end) :
    if start<end :
        mid=(start+end)//2
        Merge_sort(array,start,mid)
        Merge_sort(array,mid+1,end)
        Merge(array,start,mid,end)

if __name__=='__main__' :
    array=[2,4,5,7,1,2,3,6]
    n=len(array)
    Merge_sort(array,0,n-1)
    print(array)
    

    