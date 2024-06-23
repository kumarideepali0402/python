class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Queue:
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
        if self.isEmpty():
            self.__head=newNode
            self.__tail=newNode
            newNode.next=self.__head
        else:
           trav=trav.__head
           while trav:
               trav=trav.next
           self.__tail.next=newNode
           newNode.next=self.__head
           self.__tail=newNode
           
        self.__size+=1
    def front(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
            self.__tail=newNode
        else:
            newNode.next=self.__head
            self.__head=newNode
        self.__size+=1
    def pop(self):
        if self.isEmpty():
            raise Exception("empty")
        else:
          temp=self.__head
          self.__head=self.__head.next
          ret=temp.data

        del temp
        self.__size-=1
        return ret
    def __str__(self):
        l=[]
        trav=self.__head
        while trav:
            l.append(str(trav.data))
            trav=trav.next
        return '---->'.join(l)
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.__head.data
l=Queue()
l.push(8)
l.push(9)
print(l)