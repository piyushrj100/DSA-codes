#We will see some collision resolution techniques here 
class Hashing : 
    def __init__(self) :
         self.capacity=20
         self.hash_table=[[] for i in range(self.capacity)]

    def get_hash(self,key) :
        hash=0  
        for char in key : 
            hash+=ord(char)
        return hash % self.capacity

    def get(self,key) :
        h=self.get_hash(key) 
        for index in self.hash_table[h]:
            if index[0]==key :
                return index[1]

    def add(self,key,val) :
        h=self.get_hash(key)
        flag=False
        for index, value in enumerate(self.hash_table[h]) :
        
            if len(value)==2 and value[0]==key:
                self.hash_table[h][index]=(key,val) # updating the key value pair for an exisiting entry in the hash table 
                print(index)
                flag=True
        if not flag:
            self.hash_table[h].append((key,val))
            print(self.hash_table[h])
        
    
    def delete(self,key) :
        h=self.get_hash(key)
        for index,key_val in enumerate(self.hash_table[h]):
            if key_val[0]==key :
                del self.hash_table[h][index]
    

obj=Hashing()
obj.add("Apple",5)
obj.add("Orange",6)
obj.add("Jackfruit",9)
obj.add("Papaya",6) 
obj.add("Orange","Six")

res=obj.get("Orange")
obj.delete("Papaya")

print(obj.hash_table)
print(res)


                  
            
