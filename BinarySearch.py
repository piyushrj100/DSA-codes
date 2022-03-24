class BinarySearch :

    def binary_search(self,arr,low,high,key) :
        if high>low :
            mid=low + (high-1) // 2
        
            if arr[mid]==key :
                return mid
        
            elif arr[mid]>key :
                return self.binary_search(arr,low,mid-1,key)
        
            else :
                return self.binary_search(arr,mid+1,high,key)
        
        else :
            return -1
        

if __name__=='__main__' :
    arr=[2,5,7,21,56,89,92,99,120]
    key=92
    b_search=BinarySearch()
    search=b_search.binary_search(arr,0,len(arr)-1,key)
    
    if search == -1 :
        print(f"Key->{key} does not exist in the array ")
    else : 
        print(f"Key -> {key} found at index :{search}")

