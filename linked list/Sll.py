class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev=prev
        self.next=next
        self.data=data
class Sll:
    def __init__(self):
        self.__head=None
        
        self.__size=0
    def size(self):
        return self.__size
    def isEmpty(self):
        return self.__size==0
    
    def append(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
        else:
            trav=self.__head
            while trav.next is not None:
              trav=trav.next
            trav.next=newNode
        self.__size+=1
    
    def __str__(self):
        l=[]
        trav=self.__head
        while trav is not None:
            l.append(str(trav.data))
            trav=trav.next
        return '--->'.join(l)
    
    def addFirst(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
        else:
            newNode.next=self.__head
            self.__head=newNode
        self.__size+=1

    def addAt(self,data,index):
        if (index<0 or index>self.size()-1):
            raise Exception("Index out of bound")
        
        elif(index==0):
            self.addFirst()

        elif(index==self.__size-1):
            self.append()
        i=0
        trav=self.__head
        while i!=index:
            i+=1
            trav=trav.next
        newNode=Node(data)
        newNode.next=trav.next
        trav.next=newNode
        self.__size+=1
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List Empty")
        else:
            temp=self.__head
            self.__head=temp.next
            del temp
        self.__size-=1
    def removeLast(self):
        if self.isEmpty():
            raise Exception("List Empty")
        elif (self.size==1):
            self.removeFirst()
        else:
            i=0
            trav=self.__head
            while i!=self.__size-2:
                i+=1
                trav=trav.next
                temp=trav.next
                trav.next=None
                del temp
            self.__size-=1
    def removeAt(self,index):
        if (index<0 or index>self.size()-1):
            raise Exception("Index out of bound")
        
        elif(index==0):
            self.removeFirst()

        elif(index==self.__size-1):
            self.removeLast()
        else:
            i=0
            trav=self.__head
            while(i!=index-1):
                i+=1
                trav=trav.next
            temp=trav.next
            trav.next=trav.next.next
            temp.next=None
            del temp
        self.__size-=1
    def mid(self):
        slow=self.__head
        fast=self.__head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def search(self,element):
        i=0
        trav=self.__head
        while (trav.next is not None):
            trav=trav.next
            i+=1
            if(trav.data==element):
             return i
        return -1
    def reverse(self):
        prev=None
        curr=self.__head
        while curr is not None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.__head=prev
    def merge(self,l2):
        if not self:
            return l2
        elif not l2:
            return self
        if self.__head.data<=l2.__head.data:
            head=tail=self
            self.head=self.next
        else:
            head=tail=l2
            l2=l2.__head.next
        while self and l2:
            if self.__head.data<=l2.__head.data:
                tail.next=self
                self=self.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        if self:
            tail.next=self
        elif l2:
            tail.next=l2
        return head
    def split(self,index):
        i=0
        trav=self.__head
        while i==index:
            i+=1
            trav=trav.next
            temp=trav.next
            trav.next=None
    def interleave(self,l2):
        head=self.__head
        head2=l2.__head
        while head and head2:
            head_next=head.next
            head2_next=head2.next
            head.next=head2
            head2.next=head_next
            head=head_next
            head2=head2_next
            if head_next==None:
                break
        return self
                                               


l=Sll()
print(l.size())
print(l.isEmpty())
l.append(87)
l.append(875)
print(l)
print(l.size())
l.addFirst(54)
print(l)
print(l.size())
l.addAt(356,1)
print(l)
print(l.size())
l.removeFirst()
print(l)
print(l.size())
l.removeLast()
print(l)
print(l.size())
l.append(87)
l.append(875)
l.append(738)
print(l)
l.removeAt(1)
print(l)
print(l.size())
print(l.mid())
print(l.search(85))
l.reverse()
l.append(738)
print(l)
l2=Sll()
l2.append(78)
l2.append(780)
l2.append(784)
l2.append(738)
l2.append(73)
print(l2)
print(l.merge(l2))
print(l.interleave(l2))


        


    
    


    

    