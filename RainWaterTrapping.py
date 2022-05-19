
#takes O(n^2) time    
def naive_solution(array, size) : 
    result = 0
    for index in range(1, size-1) :
        left_max = array[index]
        for left_index in range(0, index) :
            left_max = max(left_max, array[left_index])
        right_max = array[index]
        for right_index in range(index+1, size) :
            right_max = max (right_max, array[right_index])
        result = (result + min(left_max, right_max) - array[index])
    return result 

def efficient_solution(array, size) :
    #rather than computing left max and right max everytime for each index, precompute it . Time complexity O(n). 
    # Requires auxiliary space of O(n)
    result = 0 
    left_max = [0]*size
    right_max = [0]*size
    left_max[0] = array[0]
    for index in range(1,size) :
        left_max[index] = max(array[index], left_max[index -1 ])
    right_max[size-1] = array[size -1]
    for index in reversed(range(0, size-1)) :
        right_max[index] = max (array[index], right_max[index+1])
    
    for index in range(1,size-1) :
        result = result + (min(left_max[index], right_max[index])-array[index])
    return result


if __name__ == '__main__' :
    array = [3,0,1,2,5]
    result = naive_solution(array, len(array))
    print(f'Unit of water trapped using naive approach : {result}')

    e_result = efficient_solution(array, len(array))
    print(f'Unit of water trapped using efficient approach : {e_result}')
    