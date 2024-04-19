
list=[[0,1,2],[3,4,5],[6,7,8]]
row_sum=[]
for i in range(len(list)):
    sum=0
    for j in range(len(list[i])):
        
        sum+=list[i][j]
    row_sum.append(sum)
print(row_sum)
       

