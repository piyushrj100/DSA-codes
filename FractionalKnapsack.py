class Item :
    def __init__(self,wt,val,id) :
        self.wt=wt
        self.val=val
        self.unit_cost=wt//val
        self.id=id

class FractionalKnapsack :
    def __init__(self,capacity,items) :
        self.capacity=capacity 
        self.items=items
    
    def knapsack(self) :
        self.items.sort(key=lambda u: u.unit_cost, reverse=True)
        profit=0

        for item in self.items :
            if self.capacity - item.wt >= 0 :
                self.capacity -= item.wt
                profit += item.val
            
            else :
                fraction = self.capacity/item.wt
                profit += fraction * item.val
                self.capacity= int (self.capacity - (item.wt*fraction) )
                break
        return profit

if __name__=='__main__' :
    capacity=50
    i0=Item(10,60,0)
    i1=Item(20,100,1)
    i2=Item(30,120,2)

    items=[i0,i1,i2]
    greedy_fractional=FractionalKnapsack(capacity,items) 
    total=greedy_fractional.knapsack()
    print("Total Maximum profit:", int(total))
 





    







