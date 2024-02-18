'''for i in range(7):
    for j in range(5):
        if(j==0 or j==4 or ((i==0 or i==6) and 0<j<4) ):
            print("*",end='')
        else:
            print(" ",end='')
    print()'''

def leftRotate(strr, d):
    nd=d%len(strr)
    return strr[nd:]+strr[:nd]

def rightRotate(strr, d):    
    l=len(strr)
    nd=d%len(strr)
    return strr[l-nd:]+strr[:l-nd]