class Queue :
    def __init__(self,capacity) :
        self.size=0
        self.rear=self.front=-1
        self.Q=[None]*capacity
        self.capacity=capacity

    def isFull(self) :
        return (self.rear+1) %self.capacity==self.front

    def isEmpty(self) :
        return self.front==self.rear

    def EnQueue(self,data) :
        if self.isFull() : 
            print("Queue is full")
            return
        self.rear=(self.rear+1) % (self.capacity)
        self.Q[self.rear]=data
        if self.front==-1 :
            self.front=self.rear
        self.size+=1
        

    def DeQueue(self) :
        if self.isEmpty() :
            print("Underflow! Queue is empty") 
            return
        self.Q[self.front]=None
        self.front=(self.front+1) % self.capacity 
        self.size-=1
    
    def get_front(self) :
        if self.isEmpty():
            print("Underflow! Queue is empty")
            return
        print( f'Front item is :{self.Q[self.front]}')
    
    def get_rear(self) :
        if self.isEmpty() :
            print("Underflow! Empty queue")
            return
        print(f'Rear item is : {self.Q[self.rear]}')
        

if __name__=='__main__' :
    queue = Queue(10)
    queue.EnQueue(34)
    queue.EnQueue(56)
    queue.EnQueue(5)
    queue.EnQueue(48)
    print(queue.Q) #Here None means empty slot/no element
    queue.DeQueue()
    print(queue.Q)
    queue.get_front()
    queue.get_rear()