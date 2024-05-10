class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    def __str__(self):#function which is called when we use print()
        return str(self.data)
    
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
          self.__head= newNode
          self.__tail= newNode
        else:
            self.__tail.next= newNode
            newNode.prev=self.__tail
            self.__tail=newNode
            
        self.__size+=1
    def __str__(self):
        l=[]
        trav=self.__head
        while trav is not None:
            l.append(trav.data) # l.append(str(trav.data))
            trav=trav.next
            
        return '<--->'.join(map(str,l))
    def addFirst(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
            self.__tail=newNode
        else:
            newNode.next=self.__head
            self.__head.prev=newNode
            self.__head=newNode
        self.__size+=1
    def addAt(self,index,data):
        if index<0 or index>self.size():
            raise Exception("Invalid Index")
        if index==0:
            self.addFirst(data)
        elif index==self.size:
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
        size+=1
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Can't delete from empty list")
        else:
            temp=self.__head
            self.__head=temp.next
            self.__head.prev=None
            del temp
        self.__size-=1
    def removeLast(self):
        if self.isEmpty():
            raise Exception("Can't delete from empty list")
        else:
            temp=self.__tail
            self.__tail=temp.prev
            self.tail.next=None
            del temp
        self.__size-=1
    def removeAt(self,index):
        if index<0 or index>=self.size():
            raise Exception("index out of bound")
        elif index==0:
            self.removeFirst()
        elif index==self.size()-1:
            self.removeLast()
        else:
            id=0
            trav=self.head()
            while id!=index-1:
                id+=1
                trav=trav.next
            temp=trav
            trav.next=trav.next.next
            trav.next.prev=trav
            del temp
        size-=1
    def contains(self,element):
        i=0
        trav=self.__head
        while i!=None:
            if trav.data==element:
                return True
            else :
                trav=trav.next
        return False





l1=Dll()
print(l1.size())
print(l1.isEmpty())
l1.append(23)
print(l1.size())
l1.append(45)
l1.addFirst(56)
print(l1.size())


