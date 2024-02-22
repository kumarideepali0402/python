a=[[0,0,1,1,1],[0,0,0,0,1],[0,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1]]
l=[]
for i in a:
    for j in a:
        count=0
        if(a[i][j]==1):
            count+=1
            count.append(l)
print(l)
b=max(l)



