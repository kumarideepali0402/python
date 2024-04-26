import math
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def dist(self):
        return ((self.x**2+self.y**2+self.z**2)**(1/2))
    def unit(self):
        return (self.x/self.dist(),self.y/self.dist(),self.z/self.dist())
    def get_dist(self,p):
        # return (((self.x-p.x)**2+(self.y-p.y)**2+(self.z-p.z)**2)**(1/2))
        return Point(self.x-p.x,self.y-p.y,self.z-p.z).dist()
    def is_equal(self,p):
         if((self.x==p.x) and (self.y==p.y) and(self.z==p.z)):
             return True
         else:
             return False
    def dot(self,p):
        return (self.x*p.x,self.y*p.y,self.z*p.z)
    def cross(self,p):
        return((self.y*p.z)-(self.z*p.y),((self.x*p.z)-(self.z*p.x)),(self.x*p.y)-(self.y*p.x))

    

    def rotateangle(self,theta,p):
        angle_rad= math.radians(theta)
        return((self.x-p.x)*math.cos(theta)-(self.y-p.y)*math.sin(theta))
        

    


p1=Point(1,2,3)
p2=Point(2,7,3)
print(p1.dist())
print(p1.unit())
print(p1.get_dist(p2))
print(p1.is_equal(p2))
print(p1.dot(p2))
print(p1.rotateangle(45,p2))
print(p1.cross(p2))
