class Node :
    
    def __init__(self, char) :
        self.char = char 
        #children nodes for each 26 letters of the alphabet
        self.children=[None]*26
        #checks if the word has completed at this character
        self.word_completed = False
        #checking the number of words whose prefic the character is  
        self.counter=1
    
    
    
    def contains_char(self,character) :
       return self.children[ord(character.lower())-ord('a')] != None
    
    def get_node(self,character) :
        return self.children[ord(character.lower())-ord('a')]
    
    def put_node(self,character) :
       self.children[ord(character.lower())-ord('a')] =Node(character)
       
    def setEnd(self) :
        self.word_completed= True
    
    
class Trie :
    def __init__(self) :
        self.root=Node('/')

    

    def insert_node(self, word) :
        current_node = self.root 
        for character in word :
            if  current_node.contains_char(character) is False :
               current_node.put_node(character)
            current_node = current_node.get_node(character)
        current_node.setEnd()

if __name__ == '__main__' :
    trie = Trie()
    trie.insert_node('abcd')
    print(trie.root.children[0].children[1].children[2].children[3].word_completed)







    
    
