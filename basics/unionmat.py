a=[1,2,3,4]
b=[1,5,3,6]
c=[x for x in a]
for i in b:
    
    if i not in c:
      c.append(i)

print(c)
