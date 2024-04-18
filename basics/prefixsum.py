l=list(map(int,input().split()))
t=[]
t.append(l[0])
for i in range(1,len(l)):
    t.append(l[i]+t[i-1])
    
print(t)

       