r=int(input())

for i in range(-r,r+1):
    for j in range(-r,r+1):
        
        if(((i)**2+(j)**2)**(1/2)<=r):
          print("*",end=" ")
        else:
           print(" ",end=" ")  
    print()

        
    