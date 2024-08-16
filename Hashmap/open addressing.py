class Entry:
    def __init__(self,key,value):
        self.__key=key
        self.__value=value
        self.__hash=hash(self.__key)
class HT:
    def __init__(self):
        self.__size=0
        self.__cap=12
        self.__data=[None for i in range(self.__cap)]
    def prob(self,x):
        return 5*x #P(x)=5x
    def insert(self,key,value):
        e=Entry(key,value)
        is_present=False
        index=e.hash%self.__cap
        i=0
        while(True):
            ind=index+ self.prob(i)
    if self.data[ind]==None:
        self.d