for i in range(7):
    for j in range(5):
        if (i==0 or i==6 or ((j==2) and 0<i<7)):
         print("*",end='')
        else:
           print(" ",end='')
    print()