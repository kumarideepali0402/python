a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[3,2,1],[4,2,5],[5,3,2]]
k=[[0,0,0],[0,0,0],[0,0,0]]
m,n,o=3,3,3
for i in range(m):
    
    for j in range(n):
      count=0
      sum=0
      while(count<len(a[i])):
       sum+=a[i][count]*b[count][j]
       count+=1
       k[i][j]=sum
print(k)