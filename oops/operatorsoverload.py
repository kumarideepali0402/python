class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def __add__(self,b):
        return Complex(self.real+b.real,self.img+b.img)
    
    def __sub__(self,b):
        return Complex(self.real-b.real,self.img-b.img)
    def __str__(self):
        return(f'{self.real},{self.img}i')

a=Complex(1,2)
b=Complex(3,4)
c=a+b
print(c.real,c.img)
