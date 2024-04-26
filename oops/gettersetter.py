class Point:
    def __init__(self,x,y,z):
        self.__x=x
        self.__y=y
        self.__z=z
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_z(self):
        return self.__z
    def set_y(self,newy):
        self.__y=newy
    def set_z(self,newz):
        self.__z=newz

    
    def set_x(self,newx):
        self.__x=newx

p1=Point(1,2,3)
print(p1.get_x())
print(p1.get_y())
print(p1.get_z())
p1.set_x(7)
print(p1.get_x())
p1.x=9
print(p1.get_x()) #value will reamin unchanged because it's been changed from outside


