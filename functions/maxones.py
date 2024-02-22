a=([0,1,1],[0,0,1],[1,1,1])
cols=3
i,j=0,cols-1
while(i<0 and j>=0):  
    while(a[i][j]==1):
        j-=1
        row=i
    i+=1 
print(i)        

