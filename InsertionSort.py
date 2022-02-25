def insertion(array) :
    for j in range(1,len(array)) :
        key=array[j]
        i=j-1
        while i>=0 and array[i]>key :
            array[i+1]=array[i]
            i=i-1
        array[i+1]=key

if __name__=='__main__' :
    array=[2,4,5,7,1,2,3,6]
    print(array)
    insertion(array)
    print(array)