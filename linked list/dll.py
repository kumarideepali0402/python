class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    
class Dll:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    
    def size(self):
        return self.__size
    def isEmpty(self):
        return self.__size==0
    def append(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
            self.__tail=newNode
        else:
            newNode.prev=self.__tail
            self.__tail.next=newNode
            
            self.__tail=newNode
        self.__size+=1
    def __str__(self):
        l=[]
        trav=self.__head
        while trav is not None:
            l.append(str(trav))
            trav=trav.next
            
        return '<---->'.join(l)
    
    def addFirst(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
            self.__tail=newNode
        else:
            self.__head.prev=newNode
            newNode.next=self.__head
            self.__head=newNode
        self.__size+=1

    def addAt(self,index,data):
        if(index<0 or index>self.size()):
            raise Exception("Invalid Index")
        elif index==0:
            self.addFirst(data) 
        elif index==self.size():
            self.append(data)
        else:
            id=0
            trav=self.__head
            while id!=index-1:
                id+=1
                trav=trav.next
            newNode=Node(data,trav,trav.next)
            trav.next=newNode
            newNode.next.prev=newNode
        self.__size+=1

    
l1=Dll()
l1.append(100)
print(l1.size())
l1.addFirst(10)
print(l1.size())


