list=[[0,1,2],[3,4,5],[6,7,8]]
col_sum=[]
for j in range(len(list[0])):
    sum=0
    for i in range(len(list)):
        sum+=list[i][j]
    col_sum.append(sum)
print(col_sum)
