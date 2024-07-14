# class Node:
#     def __init__(self,data,left,right,parent):
#         self.data=data
#         self.right=right
#         self.left=left
#         self.parent=parent
#     def printTree(self,node):
#         if node is None: 
#             return
#         print(node.data)
#         self.printTree(node.left)
#         self.printTree(node.right)
#     def inorder(self,node):
#         if node is None:
#             return
#         self.inorder(node.left)
#         print(node.data)
#         self.inorder(node.right)
#     def postorder(self,node):
#         if node is None:
#             return
#         self.postorder(node.left)
#         self.printTree(node.right)
#         print(node.data)

# root=Node(1,None,None,None)
# node1=Node(2,None,None,root)
# root.left=node1
# node2=Node(4,None,None,root)
# root.right=node2
# node3=Node(25,None,None,node2)
# node2.left=node3
# node4=Node(15,None,None,node2)
# node2.right=node4
# root.inorder(root)



class Node:
    def __init__(self,data,left,right,parent) -> None:
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent
    
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
    def preorder(self,node):
        if node is None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)
    def height(self,node):
        if(node.left==None and node.right==None):
            return 0
        l,r=0,0
        if(node.left!=None):
            l=self.height(node)
        if(node.right!=None):
            r=self.height(node)
        return max(l,r)+1
n=Node(1,None,None,None)
n1=Node(2,None,None,n)
n.left=n1
n2=Node(3,None,None,n)
n.right=n2
n3=Node(4,None,None,n1)
n2.left=n3
n4=Node(25,None,None,n1)
n2.right=n4
# print(n2.right.data)
n2.preorder(n2)
print(n.height(n))