a=[[1,2,3],
   [9,8,7]]
b=[[1,6],
   [9,8],
   [8,8]]
res=[[0 for x in range(len(b[0]))]for y in range(len(a))]
for i in range(0,len(a)):
    k=0
    p=0
    for j in range(0,len(b[0])):
        res[i][j]=a[i][k]*b[k][j]
        k+=1
    
print(res)