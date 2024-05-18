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
            l.append((trav.data))
            trav=trav.next
            
        return '<---->'.join(map(str,l))
    
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
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("list is empty")
        else:
            temp=self.__head
            self.__head=self.__head.next
            self.__head.prev=None
            del temp
    def removeLast(self):
        if self.isEmpty():
            raise Exception("list is empty")
        else:
            temp=self.__tail
            self.__tail=self.__tail.prev
            self.__tail.next=None
        del temp
    def removeAt(self,index):
        if self.isEmpty():
            raise Exception("List Is Empty")
        elif index==0:
            self.removeFirst()
        elif index==self.size()-1:
            self.removeLast()
        else:
            i=0
            trav=self.__head
            while i!=index-1:
                i+=1
                trav=trav.next
            temp=trav.next
            trav.next=temp.next
            trav.next.prev=trav
            del temp
    def contains(self,element):
        i=0
        trav=self.__head
        while i!=self.size():
            if(trav.data==element):
                return True
            else:
                return False
            






l1=Dll()
l1.append(23)
l1.append(67)
l1.append(61)
l1.append(84)
print(l1)
l1.removeFirst()
print(l1)
l1.removeLast()
print(l1)
l1.addFirst(213)
print(l1)
l1.removeAt(1)
print(l1)
print(l1.contains(2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        




