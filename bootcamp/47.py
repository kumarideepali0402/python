n=list(map(int,input().split()))
print(n)
adjacent_sum=[]
for i in range(len(n)-1):
    curr_sum=n[i]+n[i+1]
    adjacent_sum.append(curr_sum)
print(adjacent_sum)
