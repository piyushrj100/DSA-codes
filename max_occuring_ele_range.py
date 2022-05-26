# Maximum occurence of an element in Ranges
def max_appear(range_left, range_right, size ) :
    arr=[0]*1000
    result=0
    for i in range(0,size) :
        arr[range_left[i]] +=1
        arr[range_right[i]+1] -=1
    print(arr[0:15])
    
    #finding the prefix sum array
    maxm=arr[0]
    for i in range(1,len(arr)) :
        arr[i] +=arr[i-1]
        if maxm<arr[i] :
            maxm= arr[i]
            result=i
    print(arr[0:15])
    
    return result

if __name__=='__main__' :
    left_range=[1,2,3]
    right_range=[3,5,7]
    '''
    The range is 1-3, 2-5, 3-7

    '''
    result=  max_appear(left_range,right_range,len(left_range))
    print(result)
    # print(arr)

