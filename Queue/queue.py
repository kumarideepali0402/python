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
        else:
           self.__tail.next=newNode
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

class Stack:
    def __init__(self):
        self.Q1=Queue()
        self.Q2=Queue()
    def push(self,data):
        pass
        # self.push.q2
    def pop(self):
        pass
    def size(self):
        pass
    def isEmpty(self):
        pass
    
        



l=Queue()
l.push(2)
print(l.size())
l.push(9)
print(l)
print(l.size())
l.push(6)
print(l)
print(l.size())
print("#####")
print(l.pop())
print(l)
print(l.size())
print(l.peek())

