class Hashing :
    def __init__(self) :
        self.capacity=20
        self.hash_table=[None]*self.capacity


    def get_hash(self,key) :
        hash=0
        for char in key :
            hash+=ord(char)
        return hash%self.capacity
     
    def get(self,index) :
        h=self.get_hash(index)
        return self.hash_table[h]
    
    def add(self,key,val) : 
        h=self.get_hash(key)

        self.hash_table[h]=val

    def delete(self,key) :
        h=self.get_hash(key)
        self.hash_table[h]=None


hash=Hashing()
hash.add('hello there',76)
hash.add('Hello World',5)
hash.add("Namaste",10)
res=hash.get('hello there')

print(res)

