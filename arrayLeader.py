def find_leader(array, size) :
    leader = array[size-1] 
    l_arr= []
    l_arr.append(leader)
    for index in reversed(range(0,size-1)) :
       if leader<array[index] :
           leader=array[index]
           l_arr.append(leader)
    return l_arr[::-1]

if __name__ == '__main__' :
    array = [7,10,4,10,6,5,2]
    result = find_leader(array, len(array))
    print(f' The leaders are  : {result}')


    
