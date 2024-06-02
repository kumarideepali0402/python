class Node:
    def __init__(self,data,next=None):
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
      newNode=Node(data)
      newNode.next=self.__head
      self.__head=newNode
      self.__size+=1

   def pop(self):
      if self.isEmpty():
          raise Exception("Stack is empty")
      else:
          temp=self.__head
          k=temp
          self.__head=self.__head.next
          del(temp)
          return k.data
   def __str__(self):
      l=[]
      trav=self.__head
      while trav:
         l.append(str(trav.data))
         trav=trav.next
      return '----'.join(l)

l=Stack()
l.push(45)
l.push(98)  
l.push(65)    
print(l)
print(l.pop())



