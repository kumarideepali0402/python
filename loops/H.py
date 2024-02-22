for i in range(7):
    for j in range(5):
        if (j==0 or j==4 or ((i==3) and 0<j<4)):
         print("*",end='')
        else:
           print(" ",end='')
    print()
