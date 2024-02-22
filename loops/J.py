for i in range(7):
    for j in range(5):
        if (i==0 or (i==5 and 0<j<3) or ((j==2) and 0<i<6) or (i==4 and j==0)):
         print("*",end='')
        else:
           print(" ",end='')
    print()