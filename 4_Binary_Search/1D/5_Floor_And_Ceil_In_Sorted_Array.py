def ceils(arr,x):
    low=0
    high=len(arr)-1
    ans=-1
    while(low<=high):
        midd=(low+high)//2
        if arr[midd]>=x:
            ans=arr[midd]
            high=midd-1
        else:
            low=midd+1
    return ans

def flooor(arr,x):
    low=0
    high=len(arr)-1
    ans=-1
    while(low<=high):
        midd=(low+high)//2
        if arr[midd]<=x:
            ans=arr[midd]
            low=midd+1
        else:
            high=midd-1
    return ans

def printt(arr,x):
    m=ceils(arr,x)
    n=flooor(arr,x)
    return (m,n)
    
y=printt([3,4,7,8,8,10],5)
print(y[0],y[1])
