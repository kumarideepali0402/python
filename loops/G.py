for i in range(7):
    for j in range(7):
        if(j==0 or ((i==0 or i==6) and (0<j<5)) or ((i==3) and 2<j<6) or((i==4 or i==5) and j==4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
