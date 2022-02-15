#Queue is a linear data structure which stores items in first in first out order(FIFO)
#Enqueue: Adds an item to the queue in O(1) time
#Dequeue: removes an item from the queue in O(1) time
#Front : Returns the front item in the queue i O(1) time
#Rear: Returns the last item from the queue in O(1) time.

#Can be implemented using 
#lists
#collections.deque
#queue.Queue

#Lists are slow as inserting and deleting an element at the beginning requires
#  shifting all the other elements by 1 in O(n) time

queue=[]
queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

queue.pop(0)
queue.pop(0)
queue.pop(0)

print(queue)