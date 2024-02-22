n=int(input("enter rows:"))

for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()