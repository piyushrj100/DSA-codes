#We will be using level order traversal in a binary tree to perform operations such as Searchng,
#finding max element,number of nodes in binary tree,height of a tree

import sys

class Treenode :
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None
    
class Binary_tree :
    def __init__(self):
        self.root=None

    def get_binary_tree(self) : 
        #below are hardcoded
        self.root=Treenode(5)
        self.root.left=Treenode(4)
        self.root.right=Treenode(1)
        self.root.left.left=Treenode(8)
        self.root.left.right=Treenode(23)
        self.root.right.left=Treenode(54)
        self.root.right.right=Treenode(41)
        self.root.right.right.right=Treenode(81)
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
    
    def findmax(self,tnode,max_el=-sys.maxsize-1) :
        if tnode is None :
            return
        Q=[]
        Q.append(tnode)
        while len(Q)>0 :
            node=Q.pop(0)
            if node.data>max_el:
                max_el=node.data
            if node.left :
                Q.append(node.left)
            if node.right:
                Q.append(node.right )
        return max_el
    

    def search(self,tnode,key) :
        if tnode is None:
            return False 
        Q=[]
        Q.append(tnode) 
        while  len(Q) >0 :
            node=Q.pop(0)
            if node.data==key :
                return True
            if node.left:
                Q.append(node.left) 
            if node.right :
                Q.append(node.right)
        return False
    
    def total_nodes(self,tnode) :
        if tnode is None :
            return -1
        count=0
        Q=[]
        Q.append(tnode) 
        while len(tnode)>0:
            temp=Q.pop(0) 
            count+=1
            if temp.left:
                Q.append(temp.left) 
            if Q.right :
                Q.append(temp.right)
        return count
    
    def count_full_nodes(self,tnode) :
        if tnode is None :
            return -1
        count=0
        Q=[]
        Q.append(tnode)
        while len(Q) :
            temp=Q.pop(0)
            if  temp.left and temp.right :
                count+=1
            if temp.left:
                Q.append(temp.left) 
            if temp.right :
                Q.append(temp.right)
        return count
    
    def count_leaves (self,tnode) :
        if tnode is None :
            return -1
        count=0
        Q=[]
        Q.append(tnode)
        while len(Q) :
            temp=Q.pop(0)
            if  temp.left is None and temp.right is None :
                count+=1
            if temp.left:
                Q.append(temp.left) 
            if temp.right :
                Q.append(temp.right)
        return count
    
    def Height(self,tnode) :
        if tnode is None :
            return 
        h=0
        Q=[]
        Q.append(tnode)
        Q.append(None)
        while len(Q)>0 :
            temp=Q.pop(0)
            if temp is None :
                if(len(Q)>0) :
                    Q.append(None)
                    h+=1
            else :
                if (temp.left) :
                    Q.append(temp.left)
                if (temp.right) :
                    Q.append(temp.right)
        return h

    def max_level_sum (self,tnode) :
        if tnode is None :
             return -sys.maxsize-1
        maxsum=currsum=0
        Q=[]
        Q.append(tnode)
        Q.append(None)
        while len(Q) >0:
            temp=Q.pop(0)
            if temp is None :
                if(currsum>maxsum) :
                    maxsum=currsum
                currsum=0
                if (len(Q)>0) :
                    Q.append(None)
            else :
                currsum+=temp.data
                if (temp.left) :
                    Q.append(temp.left)
                if (temp.right) :
                    Q.append(temp.right)
        return maxsum

    def right_view(self,tnode) :
        if tnode == None :
            return
        res=[] 
        q=[]
        q.append(tnode)
        while q :
            n=len(q)
            while n>0 :
                n-=1
                temp = q.pop(0)
                if n==0 :
                    res.append(temp.data)
                if temp.left :
                    q.append(temp.left)
                if temp.right :
                    q.append(temp.right)
        return res
    
    def left_view(self,tnode) :
        if tnode==None :
            return
        q=[]
        res=[]
        q.append(tnode)
        while q :
            n=len(q)
            for i in range(1,n+1) :
                temp=q.pop(0)
                if i == 1 :
                    res.append(temp.data)
                if temp.left :
                    q.append(temp.left)
                if temp.right :
                    q.append(temp.right)
        return res


        



if __name__=='__main__' :
    tree=Binary_tree()
    tree.get_binary_tree()
    find=tree.search(tree.root,81)
    full=tree.count_full_nodes(tree.root)
    leaves=tree.count_leaves(tree.root)
    max_el=tree.findmax(tree.root)
    if find==True :
        print("Element found")
    else : 
        print("Not found") 
    print("Number of full nodes : ",full)
    print("Number of leaves:", leaves)
    print("Maximum element: ", max_el)
    h=tree.Height(tree.root)
    print("Height= ",h)
    sum=tree.max_level_sum(tree.root)
    print("Max level sum ",sum)
    right=tree.right_view(tree.root)
    print('The right view of the tree is : ', right )
    left = tree.left_view(tree.root)
    print('The left view of the tree is : ', left )

      



    
     



