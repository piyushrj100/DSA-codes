#There are three python implementations of the stack :
#List. In a threaded env, you should never use lists. lists are not thread safe 

#collections.deque--> append() and pop()  are thread safe. They are atomic operations. 
# So if you are only using ths two , then you are thread safe

#queue.LifoQueue  --> Fully thread safe

#We will be using lists here . append() can be used as push. pop()  will remove elemnts from the last 

stack_list=[]
stack_list.append(1)
stack_list.append(2) 
stack_list.append(3) 

print(stack_list)

itr=stack_list 
while itr : #this will run until the stack is empty 
    itr.pop() #this will pop an element from stack 

print(stack_list)