a=[[1,2,3],[4,5,6]]
m=len(a)
n=len(a[0])
b=[[row[j] for row in a] for j in range(n)]
print(b)
