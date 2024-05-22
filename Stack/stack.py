class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.size=0
        self.head=None
    def size(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def __str__(self):
        l=[]
        trav=self.head
        while trav is not None:
            l.append((trav.data))
            trav=trav.next
        return '--->'.join(map(str,l))
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        self.size+=1
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Underflow")
        temp=self.head
        p=self.head.data
        self.head=temp.next
        del temp
        print(p)
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack Underflow")
        print(self.head.data)


l=Stack()
l.push(56)
l.push(98)
l.push(876)
print(l)
l.pop()
print(l)
l.peek()

