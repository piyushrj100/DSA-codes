class Treenode :
    def __init__(self,val) :
        self.data=val
        self.left=None
        self.right=None
    
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

              
if __name__=='__main__' :
    tree =BST()
    tree.insert(10,tree.root)
    tree.insert(4,tree.root)
    tree.insert(11,tree.root)
    tree.insert(15,tree.root)
    tree.insert(7,tree.root)
    tree.insert(12,tree.root)
    tree.insert(16,tree.root)
    print(tree.root.data)
    tree.inorder(tree.root)
    print("\n")
    tree.preorder(tree.root)
    print("\n")
    tree.postorder(tree.root)
    res=tree.search(tree.root,90)
    print(res)
    tree.delete(tree.root,11)
    tree.inorder(tree.root)







