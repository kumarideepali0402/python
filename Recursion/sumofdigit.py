n=int(input())
sum=0
def countDigit(n):
    if(n<=0):
        return 0
    return((n%10)+countDigit(n//10))
        
    
print(countDigit(n))
