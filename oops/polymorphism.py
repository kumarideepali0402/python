#datatype as conflict breaker
class Square:
    def __init__(self,l):
        self.l=l
    def getArea(self):
        return self.l*self.l


class Circle:
    def __init__(self,r):
        self.r=r
    def getArea(self):
        return self.r*self.r*3.14



#no. of argument as conflict breaker
class Compare:
    
    def getMax(self,a,b):
        if a>b:
            return
        else:
            return b
    
    def getMax(self,a,b,c):
        if(a>b and a>c):
            return a
        elif(b>a and b>c):
            return b
        else:
            return c

a=Compare()
print(a.getMax(2,4))
print(a.getMax(2,4,9))

    