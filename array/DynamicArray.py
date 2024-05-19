class Darray:
    def __init__(self,cap:int,datatype:type)->None:
        self.__capacity=cap
        self.datatype=type
        self.__size=0
        self.__data=[None]*cap
    def __getitem__(self,index:int)->int:
        if(0<=index<self.__size):
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")
    def __setitem__(self,index:int,value:int)->int:
        if(0<=index<self.__size):
            if not isinstance(value,self.__data):
                return TypeError(f"Expected datatype{self.__datatype},got {type(value)}")
            self.__data[index]=value
        else:
            raise IndexError("Index out of range")
    def repr(self):
        return f"Dynamic Array({[self.data[i] for i in range(self.__size)]})"
        
    def get_size(self):
        return self.__size
    def get_datatype(self):
        return self.datatype
    
    def get_capacity(self):
        return self.__capacity
    def get_data(self):
        return self.__data
    def isEmpty(self):
        return self.__size==0
    def resize(self):
        newArray=[]*2*self.__capacity
        for i in range(self.__size):
            newArray[i]=self.__data[i]
            self.__capacity=2*self.__capacity
            self.__data=newArray
    def append(self,value):
        if(self.__size==self.__capacity):
            self.resize()
            self.__data[self.__size]=value
            self.__size+=1
        else:
            self.__data[self.__size]=value
            self.__size+=1
    def prepend(self,value):
        pass
        

l=Darray(5,int)
l.append(9)
l.append(87)
print(l)
repr(l)