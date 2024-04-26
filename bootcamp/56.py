n=int(input())
num=2
primes=0
while(primes<n):
    is_prime=True
    i=2
    while(i<num):
        if(num%i==0):
            is_prime=False
            break
        i+=1
    if(is_prime==True):
            print(num)
            primes+=1
    num+=1


    
      