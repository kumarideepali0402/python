a=[1,2,3]
b=[1,4,3]
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)