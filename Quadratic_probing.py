 #QP=(h(k)+ci+di^2)%m
 #let c=d=1, then 
 #QP=(h(k)+i+i^2)%m
 #m is the total capacity of the hash table.
 #h(k)=key%m

class Hashing:
    def __init__(self,capacity) :
        self.capacity=capacity
        self.hash_table=[None for i in range (self.capacity)] 

    def get_unicode(self,key):
        uni=0
        for char in key:
            uni+=ord(char)
        return uni

    def add(self,key,val) :
        code=self.get_unicode(key)
        hk=code%self.capacity
        index=0
        qp=start=hk
        while (self.hash_table[qp] and self.hash_table[qp] !=('$','$')) :
            if (self.hash_table[qp][0]==key) :
                print(f'Key {key} already exists. Value will be updated')
                self.hash_table[qp]=(key,val)
                return
            index+=1
            qp=(hk+index+index**2) % self.capacity
            if qp==start :
                print("Hash table is full! Unable to add more elements")
                return
        self.hash_table[qp]=(key,val)
    
    def search(self,key) :
        code=self.get_unicode(key)
        hk=code%self.capacity
        index=0
        qp=start=hk
        while self.hash_table[qp] :
            if self.hash_table[qp][0]==key:
                return qp
            index+=1
            qp=(hk+index+index**2) %self.capacity
            if qp==start or self.hash_table is None :
                return None
    
    def delete(self,key) :
        res=self.search(key)
        if res is None :
            print("Element is not found")
            return
        self.hash_table[res]=('$','$')


obj=Hashing(10)
obj.add("Apple",5)
obj.add("Orange",6)
obj.add("Jackfruit",9)
obj.add("Papaya",6) 
obj.add("Orange","Six")
obj.delete("Orange")
obj.add("Orange","Six")
res=obj.search("Papaya")
obj.add("Mango",5)
print(obj.hash_table[res][1])

print(obj.hash_table)
    

        




    
          