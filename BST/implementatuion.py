class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        
class BST:
    def __init__(self):
        self.root=None
        # self.size=0
    def insert2(self,root,data):
        #insert value in myBST and return the update tree
        if(root==None):
            return Node(data)
        if(root.data==data):
            return root
        if(data<root.data):
            root.left=self.insert(root.left,data)
            return root
        else :
            root.right=self.insert(root.right,data)
            return root
        
    def insert(self,data):
        self.root=self.insert2(self.root,data)
        return self.root.data
    
    
    def inorder(self,root):
        if(root==None): 
            return
        self.inorder(self.left)
        print(root.data)
        self.inorder(self.right)

    def printTree(self):
        self.inorder(self.root)
    
    def remove(self,data):
        self.root=remove2(self.root,data)
    def remove2(self,root,data):
        if(root==None):
            return root
        if(root.data>data):
            root.left=self.remove2(root.left,data)
            return root
        if(root.data<data):
            root.right=self.remove2(root.right,data)
            return root
        if(root.data==data):
            if(root.left==None and root.right==None):
                del root
                return None
            if(root.right==None ):
                temp=root.left
                del root
                return temp
            if(root.left==None):
                temp=root.right
                del root
                return temp
            else:
                succ=root.left
                while succ.right is not None:
                    succ=succ.right
                root.data=succ.data
                remove2(succ.data)
            







newnode=Node(13)
print(newnode.data,newnode.left,newnode.right)
newnode.insert(12)
newNode.print()