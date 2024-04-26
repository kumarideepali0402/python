def multiply_matrices(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j]+=a[i][k]*b[k][j]
    return c

def power(a,n):
    if(n==1):
        return a
    elif(n%2==0):
        return(power(multiply_matrices(a,a),n//2))
    return(multiply_matrices(a,power(multiply_matrices(a,a),(n-1)//2)))

def fibonacci(n):
    if(n==0):
        return 0
    
    k=[[1,1],[1,0]]
    return power(k,n-1)[0][0]

n=int(input())
print(fibonacci(n-1))

