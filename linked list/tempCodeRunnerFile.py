def search(self,element):
        i=0
        trav=self.__head
        while (trav.data!=element):
            trav=trav.next
            i+=1
        return i+1