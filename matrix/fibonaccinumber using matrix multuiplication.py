def multiply_mat(a,b):
    res=[[0 for x in range(len(b[0]))]for y in range(len(a))]

    for i in range(0,len(a)):
     for j in range(0,len(b[0])):
        for k in range(0,len(b[0])):
          res[i][j]+=(a[i][k]*b[k][j])
        
    return res
def power(p,i):
   if(i==0):
      return [[1,0],[0,i]]
   if(i==1):
      return p
   if(i%2==0):
      return(power(multiply_mat(p,p),i//2))
   return (multiply_mat(p,power(p,(i-1)//2)))
      
      