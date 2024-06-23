class Entry:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.hash=hash

class Hashmap:
    def __init__(self,size,cap,max_threshold):
        self.__size=0
        self.__cap=cap
        self.__data=[[] for i in range(cap)]
        self.__max_threshold=max_threshold

    def size(self):
        return self.__size
    def isEmpty(self):
        return self.__size==0
    def resize(self):
        new_cap=2*self.__cap
        new_data=[[] for i in range(new_cap)]
        for i in range(self.__cap):
            for e in (self.__data[i]):
                new_hash=hash(e.key)%new_cap
                new_data[new_hash].append(Entry(e.key,e.value,e.hash))
        del self.__data
        self.__data==new_data
        self.__cap=new_cap

    
    def insert(self,key,value):
        if((self.__size/self.__cap)>=self.__max_threshold):
            self.resize()
        e=Entry(key,value,hash(key)%self.__size)
        is_present=False
        for i in range(self.__data[e.hash]):
            if(self.__data[e.hash][i].key==e.key):
                self.__data[e.hash][i]=e
                is_present=True
            if(not is_present):
                self.__data[e.hash].append(e)
            self.__size+=1


    def get(self,key):
        index=hash(key)%self.__cap
        for e in self.__data:
            if(e.key==key): 
                return e.value
            return None
        
    def remove(self,key):
        index=hash(key)%self.__cap
        for e in self.__data:
            if (e.key==key):
                self.__data[index].remove(e)
                self.__size-=1
                break
                



a=Hashmap(4,6,8)
a.insert(2,"deepali")
print(a.__size)  
