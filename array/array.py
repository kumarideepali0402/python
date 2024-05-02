from typing import TypeVar
T=TypeVar('T')
class myArray:
    def __init__(self,cap:int,datatype:type)->None:
        self.__capacity=cap
        self.__size=0
        self.__data=[None]*cap
        self.type=type
    def get_capacity(self):
        return self.__capacity
    def get_size(self):
        return self.__size
    def get_data(self):
        return self.__data
    def get_type(self):
        return self.datatype



    def __getitem__(self,index:int)->int:
        if(0<=index<self.__size):
          return self.data[index]
        else:
          raise IndexError("Index out of bounds")
    
    def __setitem__(self,index:int,value:int)->int:
        if(0<=index<self.__size()):
            if not isinstance(value,self.__data):
                raise TypeError(f"Expected datatype{self.__datatype},got{type(value)}")
            self.__data[index]=value
        else:
            raise IndexError("Index out of bounds")
    
    def __len__(self):
        return self.__size
    
    def __resize(self):
        newarray=[]*2*self.__capacity
        for i in range(self.__size):
            newarray[i]=self.__data[i]
            self.__capacity=2*self.__capacity
            self.__data=newarray
    
    def append(self,value):
        if self.__size<self.__capacity:
            self.__data[self.__size]=value
            self.__size+=1
        else:
            self.__resize()
            self.__data[self.__size]=value
            self.__size+=1
        
    
    




