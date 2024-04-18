import math
n=int(input())
power=math.log2(n)
l=math.floor(power)
u=math.ceil(power)
if(power-l<u-power):
    print(2**l)
else:
    print(2**u)
        
