# # without init
# class Vehicle:
#     def display(self):
#         print("I'm a Vehicle.")

# class Car(Vehicle):
#     def m(self):
#         print("I'm a Car.")
#         super().display()
# c=Car()
# print(c.m()) 
# print(c.display())
# with init
# class Shape:
#     def __init__(self,sides):
#         self.sides=sides
#     def get_no_of_sides(self):
#         return self.sides

# class Square(Shape):
#     def __init__(self,len):
#         self.len=len
#         super().__init__(4)
# k=Square(29)
# print(k.get_no_of_sides())
# print(k.len)
# print(k.sides)

# multiple level of inheritance
class Shape:
    def __init__(self,sides):
        self.sides=sides
class Quadrilateral(Shape):
    def __init__(self,a1,a2,sides):
      self.a1=a1
      self.a2=a2
      super.__init__(sides)
class Square(Quadrilateral):
    def __init__(self,length,a1,a2,sides):
        self.length=length
        super.__init__(a1,a2,sides)
class Parallelogram(Quadrilateral):
    pass
class Rectangle(Quadrilateral):
    pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(0)
        # p1.init


k=Square(20,90,90,4)
print(k.length)

