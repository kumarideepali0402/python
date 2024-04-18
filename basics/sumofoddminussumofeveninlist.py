l=list(map(int,input().split()))
se=0
so=0
for i in range(0,len(l)):
    if(i%2==0):
        se+=l[i]
    else:
        so+=l[i]
print(so-se)
