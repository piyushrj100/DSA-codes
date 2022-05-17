class Node :
    
    def __init__(self, char) :
        self.char = char 
        #children nodes for each 26 letters of the alphabet
        self.children=[None]*26
        #checks if the word has completed at this character
        self.word_completed = False
        #checking the number of words whose prefic the character is  
        self.counter=1
    
    @staticmethod
    def get_index(character) :
        return ord(character.lower())-ord('a')

    def contains_char(self,character) :
       #checks if the index in children is null or contains an object.  
       return self.children[Node.get_index(character)] != None
    
    def get_node(self,character) :
        #returns the node object present at the index in children
        return self.children[Node.get_index(character)]
    
    def add_node(self,character) :
        #adds a new node in children list at the particular index 
       self.children[Node.get_index(character)] =Node(character)
       
    def set_end(self) :
        self.word_completed= True
    
    def unset_end(self) :
        self.word_completed = False
    
    
class Trie :
    def __init__(self) :
        self.root=Node('/')

    

    def insert_word(self, word) :
        current_node = self.root 
        for character in word :
            if  current_node.contains_char(character) is False :
                current_node.add_node(character)
            current_node = current_node.get_node(character)
            
        current_node.set_end()
    
    def search_word(self, word) :
        current_node = self.root
        for character in word :
            if current_node.contains_char(character) is False :
                return None
            current_node = current_node.get_node(character)
        return current_node
    
    def delete_word(self, word) :
        node = self.search_word(word) 
        if node is not None :
            node.unset_end()      

    #returns true if words starting with a prefx is present --O(len)
    def starts_with(self, prefix) :
        current_node = self.root 
        for character in prefix : 
            if current_node.contains_char(character) is False :
                return False 
            current_node = current_node.get_node(character) 
        return True


if __name__ == '__main__' :
    trie = Trie()
    trie.insert_word('abcd')
    trie.insert_word('ab')
    trie.insert_word('PiYuSh')

    #prints the  wrd_end for 'd' node of 'abcd' , After insertion  it should be set to True
    print(trie.root.children[0].children[1].children[2].children[3].word_completed)
    search = trie.search_word('abcd')
    print(search.__dict__)
    search = trie.search_word('ab')
    print(search.__dict__)
    search = trie.search_word('PiYuSh')
    print(search.__dict__)
    trie.delete_word('abcd')
    print(f" Starts with jkl ?? {trie.starts_with('jkl')}")
    print(f" Starts with Pi ?? {trie.starts_with('Pi')}")
    #prints the  word_end for 'd' node of 'abcd' , After deleting it should be set to False
    print(trie.root.children[0].children[1].children[2].children[3].word_completed)







    
    
