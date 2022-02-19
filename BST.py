class Treenode :
    def __init__(self,val) :
        self.data=val
        self.left=None
        self.right=None


############################################################## Method Description ###############################################################
#                                                                                                                                               #
# insert()              :      Inserts an element in the tree. Arguments: key , root node                                                       #
# inorder()             :      Prints the inorder tree traversal of the tree. Arguments: root node.                                             #
# postorder()           :      Prints the postorder tree traversal of the tree. Arguments: root node.                                           #
# preorder()            :      Prints the preorder tree traversal of the tree. Arguments: root node.                                            #
# search()              :      Returns true if the given element is found . Arguments: root node, search key                                    #
# inorder_successor()   :      Returns the inorder successor of a particular node. Arguments: right subtree node                                #
# delete()              :      Deletes the element if it is present in the tree. Returns None if not found. Arguments: root node,key            #
# height()              :      Finds the height of the tree. Arguments: root node                                                               #
# level_order()         :      Prints the level order traversal of the tree.                                                                    #
# is_path_sum()         :      Returns True if the sum from root to leave is equal to the integer provided. Arguments : root node, integer.     # 
#                                                                                                                                               #
#################################################################################################################################################
class BST :
    def __init__(self) :
        self.root=None

    def insert(self,key,node) :
        if node is None :
            self.root=Treenode(key)
            return
        if key==node.data :
            print("Value already exists")
            return
        if key<node.data :
            if node.left is None :
                node.left=Treenode(key)
            else:        
                self.insert(key,node.left)

        if key>node.data :
            if node.right is None:
                node.right=Treenode(key)
            else:
                self.insert(key,node.right)
    
    def inorder(self,node) :
        if node :
            self.inorder(node.left)
            print(node.data," ",end="") 
            self.inorder(node.right)
    def postorder(self,node) :
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data," ",end="") 
    def preorder(self,node) :
        if node :
            print(node.data," ",end="") 
            self.preorder(node.left)
            self.preorder(node.right)
    
    def search(self,node,key) :
        if node is None :
            return False
        if key==node.data :
            
            return True

        if key<node.data :
            return self.search(node.left,key)
        if key>node.data:
            return self.search(node.right,key)
        return False
    
    def inorder_successor(self,node) :
        temp=node
        while temp.left is not None:
            temp=temp.left
        return temp
    
        
    def delete(self,node, key):
        found=self.search(node,key)
        if found==False :
            return None
 
        if node is None:
            return node
 
        if key < node.data:
            node.left = self.delete(node.left, key)
 
        elif(key > node.data):
            node.right = self.delete(node.right, key)
 
        else:
 
        # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
 
            elif node.right is None:
                temp = node.left
                node = None
                return temp
 
        
            temp = self.inorder_successor(node.right)
            node.data = temp.data
 
        # Delete the inorder successor
            node.right = self.delete(node.right, temp.data)
 
        return node
    
    def height(self,node) :
        if node is None :
            return -1 
        lh=self.height(node.left)
        rh=self.height(node.right)
        return (max(lh,rh)+1)

    def level_order(self,node) :
        if node is None :
            return
        Q=[]
        Q.append(node)
        while len(Q) >0   :
            # print(len(Q)) 
            print(Q[0].data," ",end="")
            temp=Q.pop(0)
            if temp.left is not None :
                Q.append(temp.left)
            if temp.right is not None :
                Q.append(temp.right )
        
    def is_path_sum(self,node,sum) :
        if node is None :
            return(sum==0) 
        temp=sum-node.data
        return(self.is_path_sum(node.left,temp) or self.is_path_sum(node.right,temp) )
            
  
              
if __name__=='__main__' :
    tree =BST()
    tree.insert(10,tree.root)
    tree.insert(4,tree.root)
    tree.insert(11,tree.root)
    tree.insert(15,tree.root)
    tree.insert(7,tree.root)
    tree.insert(12,tree.root)
    tree.insert(16,tree.root)

    #Tree  after all insertions : `  `

    ''' 
            10
            / \
            4  11
             \   \
              7  15
                  / \
                  12 16
                  
                  '''

    # print(tree.root.data)
    print("Inorder-->"," ",end="")
    tree.inorder(tree.root)
    print("\nPreorder-->"," ",end="")
    tree.preorder(tree.root)
    print("\nPostorder-->"," ",end="")
    tree.postorder(tree.root)
    res=tree.search(tree.root,90)
    if res ==True :
        print("\nElement found")
    else :
        print("\nNot Found")
    d=tree.delete(tree.root,11)
    if d is None :
        print("Unable to delete! Element does not exist")
    else : 
        print("Element deleted!!")
    
    #Tree after deletion :
    '''
            10
            / \
           4   15
            \  / \
             7 12 16

                  '''
    print("Inorder-->"," ",end="")   
    tree.inorder(tree.root)
    print(f"\nHeight of the tree: {tree.height  (tree.root)}")
    tree.level_order(tree.root)
    is_sum=tree.is_path_sum(tree.root,211)
    if is_sum :
        print("\nPath has the given sum!")
    else :
        print("\nNo path has the given sum!")
    








