class Student():
    exams_given=[] #class level datatype(declared globally)
    def __init__(self,id,name):
        self.books=[]
        self.rollno=id
        self.name=name
        self.college="ab"#object/instance level datatype can be different for different obect
st1=Student(5,"abc")
st2=Student(7,"cfg")
st1.books.append("w")
st2.books.append("k")
st1.exams_given.append("jee")
st2.exams_given.append("neet")
st1.college="cd"

print(st1.rollno)
print(st2.rollno)
print(st1.exams_given)
print(st2.exams_given)
print(st1.college)
print(st2.college)


