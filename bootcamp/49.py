# i=int(input())
# j=int(input())
# l=[[0]*j]*i
list=[[0,1,2],[3,4,5],[6,7,8]]
row_sum=[]

for i in list:
    for j in range(len(i)):
        sum=0
        sum+=list[i][j]
        row_sum.append(sum)



        
print(row_sum)
       

