for i in range(0,7):
    for j in  range(0,5):
        if(((j==0) and (i!=0 and i!=6)) or (((i==0) or (i==6)) and (0<j))):
         print("*",end='')
    
        else:
         print(" ",end='')
    print()

        