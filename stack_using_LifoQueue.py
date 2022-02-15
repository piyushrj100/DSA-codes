#There are many other methods in deque class which are not atomic. 
#So queue.LifoQueue is preferred as it is thread safe.
 
from queue import LifoQueue

stack=LifoQueue()
stack.put(1)
stack.put(23)
stack.put(23)

print(stack)

stack.get()
stack.get()
stack.get()
# stack.get() #waits forever 
#use the below to avoid the wait

stack.get_nowait()
