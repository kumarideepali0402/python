class Node:
    def __init__(self,data,next=None)
     self.data=data
     self.next=next
class Stack:
    def __init__(self):
     self.__head=None
     self.__tail=None
     self.__size=0
    def size(self):
       return self.__size
    
    def isEmpty(self):
       return self.size()==0
    
    def push(self,data):
        newNode=Node()
        if self.isEmpty():
          self.__head=newNode
          self.__tail=newNode
        else:
          self.__tail.next=newNode
          self.__tail=newNode

    def pop(self):
       if self.isEmpty():
          raise Exception("Stack is empty")
       else:
          trav=self.__head
          while trav.next.next:
             trav=trav.next
          trav.next=None
          self.__tail=trav

l=Stack()
l.push()
       


