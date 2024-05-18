class Node:
    def __init__(self,data,prev=None,next=None):
      self.data=data
      self.prev=prev
      self.next=next
class Sll:
    def __init__(self):
        self.__head=None

    def append(self,data):
        trav=self.__head
        while trav.next is not None:
            trav=trav.next
        newNode=Node(data)
        trav.next=newNode

    def __str__(self):
        l=[]
        trav=self.__head
        while trav is not None:
            l.append(trav)
        trav=trav.next

    
l=Sll()
l.append(23)
l.appendf(87)
l.append(76)
print(l)





