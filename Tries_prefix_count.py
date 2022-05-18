class Node :

    def __init__(self) :
    
        self.children = [None]*26
        self.count_word_end_with = 0
        self.count_prefix = 0
    
    @staticmethod
    def get_index(character) :
        return ord(character.lower())-ord('a')
    
    def get_node(self, character) :
        return(self.children[Node.get_index(character)])
    
    def contains_char(self,character) :
        return (self.children[Node.get_index(character)] != None)
    
    def add_node(self, character) :
        self.children[Node.get_index(character)] = Node()
    
    def increase_end(self) :
        self.count_word_end_with +=1

    def increase_prefix(self) :
        self.count_prefix +=1
    
    def reduce_prefix(self) :
        self.count_prefix -=1
    
    def delete_end(self) :
        self.count_word_end_with -=1
    
    def get_prefix(self) :
        return self.count_prefix
    def get_end(self) :
        return self.count_word_end_with


class Trie :
    def __init__(self) :
        self.root = Node()
    
    #O(len) time complexity 
    def insert_word(self,word) :
        current_node = self.root
        for character in word :
            if current_node.contains_char(character) is False :
                current_node.add_node(character)
            current_node = current_node.get_node(character) 
            current_node.increase_prefix()
        current_node.increase_end() 
    
    #O(len) time complexity
    def count_prefix_words(self, prefix) :
        current_node = self.root 
        for character in prefix :
            if current_node.contains_char(character) :
                current_node = current_node.get_node(character)
            else :
                return 0 
        return current_node.get_prefix()
    
    def count_words(self, word) :
        current_node = self.root 
        for character in word : 
            if current_node.contains_char(character) :
                current_node = current_node.get_node(character) 
            else :
                return 0
        return current_node.get_end()
    
    #o(len) time complexity 
    def delete_word(self, word) :
        current_node = self.root 
        for character in word :
            if current_node.contains_char(character) :
                current_node = current_node.get_node(character) 
                current_node.reduce_prefix()
            else : 
                return 
        current_node.delete_end()
    
    def search_word(self,word) :
        current_node = self.root
        for character in word :
            if current_node.contains_char(character) is False :
                return False 
            current_node =current_node.get_node(character) 
        return True 


if __name__ == '__main__' :
    trie = Trie()
    #inserting words in the dictionary 
    trie.insert_word('mango')
    trie.insert_word('man')
    trie.insert_word('mango')
    trie.insert_word('man')
    trie.insert_word('m')

    #count words starting with 'ma'
    count_prefix = trie.count_prefix_words('ma')
    print(f'Words starting with ma--> {count_prefix}')
    count_prefix = trie.count_prefix_words('mang')
    print(f'Words starting with mang--> {count_prefix}')
    count_prefix = trie.count_prefix_words('abc')
    print(f'Words starting with abc--> {count_prefix}')

    #counting euqal words 

    count_equal = trie.count_words('mango')
    print(f' no of words equal to mango -->{count_equal}')
    count_equal = trie.count_words('xyz')
    print(f' no of words equal to xyz -->{count_equal}')

    #deleting
    trie.delete_word('man')
    trie.delete_word('mango')
    count_equal = trie.count_words('mango')
    print(f' no of words equal to mango -->{count_equal}')
    count_equal = trie.count_words('man')
    print(f' no of words equal to man -->{count_equal}')
    count_prefix = trie.count_prefix_words('mango')
    print(f'Words starting with mang--> {count_prefix}')
    count_prefix = trie.count_prefix_words('man')
    print(f'Words starting with man--> {count_prefix}')

    #searching 
    print(f"Is word fgh present ? {trie.search_word('fghj')}")
    print(f"Is word fgh present ? {trie.search_word('mango')}")










            

    

