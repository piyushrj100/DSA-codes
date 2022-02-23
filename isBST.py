#check if the given tree is a BST or not 
# INT_MIN=-sys.maxsize-1
# INT_MAX=sys.maxsize
import sys

class Treenode :
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
class Binarytree:
    def __init__(self):
        self.root=None
    def isBST(self,tnode,minm,maxm) :
        if tnode is None:
            return True
        if tnode.data<minm or tnode.data>maxm :
            return False
        
        return ( self.isBST(tnode.left,minm,tnode.data-1) and self.isBST(tnode.right,tnode.data+1,maxm) )

        
    def inorder(self,root) :
        if root is None :
            return
        self.inorder(root.left)
        print(root.data," ",end="")
        self.inorder(root.right)


tree_1 =Binarytree()
tree_1.root=Treenode(5)
tree_1.root.left=Treenode(4)
tree_1.root.right=Treenode(1)
tree_1.root.left.left=Treenode(8)
tree_1.root.left.right=Treenode(23)
tree_1.root.right.left=Treenode(54)
tree_1.root.right.right=Treenode(41)
tree_1.root.right.right.right=Treenode(81)

#Tree formed :
'''

                 5
                / \
               4   1  
              / \  / \
             8  23 54 41
                        \
                         81
        
'''

tree_2=Binarytree()
tree_2.root=Treenode(9)
tree_2.root.left=Treenode(7)
tree_2.root.right=Treenode(21)
tree_2.root.left.left=Treenode(6)
tree_2.root.left.right=Treenode(8)
tree_2.root.left.left.left=Treenode(3)
tree_2.root.right.left=Treenode(14)
tree_2.root.right.right=Treenode(24)
tree_2.root.right.right.left=Treenode(22)
tree_2.root.right.right.right=Treenode(30)

#Tree formed
'''
        9
       /  \
      7    21
    / \   /  \
   6   8 14  24
  /          /  \
 3          22  30

'''

# (tree_1.IsBST(tree_1.root))
# print(tree_2.IsBST(tree_2.root))
# tree_2.inorder(tree_2.root)
 
res=tree_1.isBST(tree_1.root,-sys.maxsize-1,sys.maxsize)
print(res)
res=tree_2.isBST(tree_2.root,-sys.maxsize-1,sys.maxsize)
print(res)
 



