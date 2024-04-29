class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def __add__(self,b):
        return Complex(self.real+b.real,self.img+b.img)
    
    def __sub__(self,b):
        return Complex(self.real-b.real,self.img-b.img)
    def __mul__(self,b):
        return Complex(self.real*b.real,self.img*b.img)
    def __lt__(self,b):
        if(self.real>b.real):
            return b
        elif(self.real==b.real):
            print("equal")
        else:
            return a
    def __truediv__(self,b):
        deno=(b.real)**2+(b.img)**2
        realpart=((self.real*b.real)+(self.img+b.img))/deno
        imgpart=((self.img*b.real)-(self.real*b.img))/deno
        
        return Complex(realpart,imgpart)
a=Complex(9,5)
b=Complex(8,7)
c=a+b
# print(c)
print(c.real,c.img)
s=a-b
print(s.real,s.img)
d=a*b
print(d.real,d.img)
e=a<b
print(e.real)
f=a/b
print(f.real,f.img)