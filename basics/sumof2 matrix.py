a=[[1,2,3],[2,3,4]]

b=[[5,6,7],[4,3,2]]
res=[x for x in range(len(a[0]))for y in range(len(a))]

for i in range(0,len(a)):
    for j in range(0,len(a[0])):
      res[i][j]=a[i][j]+b[i][j]
print(res) 


