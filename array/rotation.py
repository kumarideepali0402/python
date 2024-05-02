def rotateArray(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr
arr=[0,1,2,3,4,5]
d=int(input("enter pivot point:"))
n=len(arr)+1
k=rotateArray(arr,d,n)
print(k)