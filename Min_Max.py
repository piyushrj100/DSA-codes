#Simultaneous Minimum and Maximum. The below code will find the simultaneous maximum and minimum in less than 2(n-1) comparisons.
#Compare pair of elements with each other first and then with the maximum and minimum element. 
# Total 3 comparision needed for 2 elements. 
#If n is odd, make the first element as max and minimumm and then follow the above step in pairs . Total 3*(floor(n/2)) comparison.
# If n is even, first element is set to be minimum and second element is sert to be max. Process the rest of the elements in pairs.
#Total 3(n-2) -2 comparisons required. In either case total comparisions is at most 3*(floor(n/2)).

def Even_min_max(array) :
    count=0
    minimum=min(array[0],array[1])
    maximum=max(array[0],array[1])
    for i in range(2,len(array),2) :
        count+=1
        min_idx=i+1
        max_idx=i
        if  array[i] <=array[i+1]  :
            min_idx=i
            max_idx=i+1
        minimum=min(array[min_idx],minimum)
        maximum=max(array[max_idx],maximum)
        count+=2
    print(minimum,maximum,count)
    print(f"Minimum= {minimum}, Maximum = {maximum}, Total comparisons(Excluding initial)={count}")


def Odd_min_max(array) :
    count=0 # number of comparisons
    minimum=maximum=array[0]
    for i in range (0,arr_len-1,2) :
        count+=1
        min_idx=i+1
        max_idx=i
        if  array[i] <=array[i+1]  :
            min_idx=i
            max_idx=i+1
        minimum=min(array[min_idx],minimum)
        maximum=max(array[max_idx],maximum)
        count+=2
    print(minimum,maximum,count)
    print(f"Minimum= {minimum}, Maximum = {maximum}, Total comparisons={count}")

array=[3,75,232,2,2,4,7,4,4,57,4,75,2,6,28,48,-9,-23,34,654]
arr_len=len(array)
if arr_len % 2==1 :
    Odd_min_max(array)
else :
    Even_min_max(array)
        
