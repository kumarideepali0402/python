class Node:
    def __init__(self,data,prev=None,next=None,trav=None):
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
        self.__size+=1
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
            (self.__tail).next=None
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
            trav=self.__head
            while id!=index-1:
                id+=1
                trav=trav.next
            temp=trav.next
            trav.next=trav.next.next
            trav.next.prev=trav
            del temp
        self.__size-=1
    def contains(self,element):
        i=0
        trav=self.__head
        while i!=None:
            if trav.data==element:
                return True
            else :
                trav=trav.next
        return False
    def __iter__(self):
        self.__trav=self.__head
        return self
    def __next__(self):
        x=self.__trav.data
        if trav.next is None:
            raise StopIteration
        else:
            self.__trav=self.__trav.next
            return x
    def findMid(self,head):
        if head is None:
            return None
        slow=head
        fast=head
        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
        return slow







l1=Dll()
l1.append(23)
l1.append(45)
l1.append(87)
print(l1)
l1.addFirst(62)
print(l1)
l1.addAt(2,45)
print(l1)
l1.removeFirst()
print(l1)
l1.removeLast()
print(l1)
l1.removeAt(2)
print(l1)
print(l1.contains(45))
l1.append(45)
l1.append(87)
print(l1)
l1.append(87)
l1.findMid(self.__head)

