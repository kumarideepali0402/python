n=int(input())
s=""
while(n):
    s+=str(n%2)
    
    n=n//2
print(s[::-1])



