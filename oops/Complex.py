class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def __add__(self,b):
        return Complex(self.real+b.real,self.img+b.img)
    
    def __sub__(self,b):
        return Complex(self.real-b.real,self.img-b.img)
    def __mul__(self,b):
        return Complex(a*b)
a=Complex(9,5)
b=Complex(8,7)
c=a+b
print(c)