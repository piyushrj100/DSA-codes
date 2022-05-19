# problem link :  https://bit.ly/3n3kedU
#


class Node :

    def __init__(self) :
        self.children = [None]*26
        self.word_completed = False 

    @staticmethod
    def get_index(character) :
        return ord(character.lower()) - ord('a')
    
    def contains_char(self, character) :
        return self.children[Node.get_index(character)] != None
    
    def get_node(self, character) :
        return self.children[Node.get_index(character)]
    
    def add_node(self, character) :
        self.children[Node.get_index(character)] = Node()
    
    def set_end(self) :
        self.word_completed = True
    
    def unset_end(self) :
        self.word_completed = False

    def get_end_status(self) :
        return self.word_completed



class Trie() :
    def __init__(self) :
        self.root = Node()
    
    def insert_word(self, word) :
        current_node = self.root 
        for character in word :
            if current_node.contains_char(character) is False :
                current_node.add_node(character) 
            current_node = current_node.get_node(character)
        current_node.set_end()
    
    def check_all_prefix_exists(self, word) :
        flag = True
        current_node = self.root 
        for character in word   :
            if current_node.contains_char(character) :
                current_node =current_node.get_node(character)
                if current_node.get_end_status() is False :
                    flag = False 
                    break
            else :
                return False
        return flag
    
    def insert_word_list(self, word_list) :
        for word in word_list :
            self.insert_word(word) 

    def check_longest_word_all_prefix(self,word_list) :
        longest_word = ""
        self.insert_word_list(word_list)
        for word in word_list :
            if self.check_all_prefix_exists(word) :
                if len(word) > len(longest_word) :
                    longest_word = word
                elif len(word) == len(longest_word) and word < longest_word :
                    longest_word = word 
        
        if longest_word == "" :
            return None 
        return longest_word

if __name__ == '__main__' :
    word_list =['a', 'ap', 'app', 'appl', 'apple','apple', 'apply']
    trie = Trie()
    result = trie.check_longest_word_all_prefix(word_list)
    print(result)

    






