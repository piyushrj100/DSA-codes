class Hashing :
    def __init__(self,capacity) : 
        self.capacity=capacity
        self.hash_table=[None for i in range(self.capacity)]

    def get_unicode(self,key):
        uni=0
        for char in key:
            uni+=ord(char)
        return uni
        
    
    def add(self,key,val):
        code=self.get_unicode(key)
        h=code%self.capacity
        start=hs=h
        index=0
        while self.hash_table[hs]  and self.hash_table[hs] !=('$','$'):
            if(self.hash_table[hs][0]==key) : #This will update the value for an existing item 
                print(f"Key {key} already exists.Value will be updated")
                self.hash_table[hs]=(key,val)
                return
            index+=1
            hs=(h+index)%self.capacity
            
            if hs==start :
                print("Hash Table is full")
                return
        self.hash_table[hs]=(key,val)

    def search(self,key) :
        code=self.get_unicode(key)
        h=code%self.capacity
        index=0
        hs=start=h
        while self.hash_table[h] :

            if self.hash_table[hs][0]==key :
                return hs

            index+=1
            hs=(h+index)%self.capacity
            if start==hs or  self.hash_table[hs] is None :
                return None
    def delete(self,key) :
        res=self.search(key)
        if res is None : 
            print("Element not found")
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
print(obj.hash_table[res][1])

print(obj.hash_table)


    
        

        




        
            







    # def get_hash(self,key) :
    #     hash=self.get_unicode(key)
    #     h=hash%self.capacity
    #     for index in range(self.capacity) :
    #         if (h+index)%self.capacity==(None or '$') :
    #             return (h+index)%self.capacity
    
    # def add(self,key,val) :
    #     h=self.get_hash(key)
    #     if h is None :
    #         print("No space available")
    #         return
    #     self.hash_table[h]=val

    # def search(self,key,val) :
    #     ucode=self.get_uni(key)
    #     h=ucode%self.capacity
    #     lp=h
    #     for idx in range(self.capacity) :
    #         if self.hash_table[lp] is not None and self.hash_table[lp] != val:
    #             lp=(h+idx) % self.capacity
    #     if self.hash_table[lp]==val:
    #         return val
    #     else :
    #         return None
    
    # def delete(self,key):
    #     find=self.search()




            













