a=list(map(int,input().split()))
for i in range(0,len(a)-3):
   if(a[i+3]==a[i+2]+a[i+1]):
      flag=1
   else:
      flag=0
if(flag==1):
      print("yes")
else:
      print("no")


