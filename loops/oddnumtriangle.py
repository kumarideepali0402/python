n=int(input("enter a number:"))
for i in range(0,n):
    for j in range(0,i+1):
        print(2*j+1,end='')
    print()              