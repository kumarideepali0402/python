def bs(arr,high,low,x):
    if low<=high:
        mid=(high+low)//2
        if arr[mid] ==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
            return bs(arr,high,low,x)
        elif arr[mid]<x:
            low=mid+1
            return bs(arr,high,low,x)
    else:
        return -1
    arr=[1,2,3,4,5,8,9]
    x=4
    result=bs(arr,len(arr)-1,0,x)
    if result!=-1:
        print("element is present at index:",str(result))
    else:
        print("not present")

