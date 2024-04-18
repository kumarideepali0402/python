l=int(input())
b=int(input())
for i in range(l):
    for j in range(b):
        if(i==0 or i==l-1 or j==0 or j==b-1):
         print('* ',end="")
        else:
           print(" ",end=" ")
    print()