def searchInsert(arr: [int], m: int) -> int:
    # Write your code here.
    low=0
    high=len(arr)-1
    ans=len(arr)
    while (low<=high):
        midd=(low+high)//2
        if arr[midd]>=m:
            ans=midd
            high=midd-1
        else:
            low=midd+1
    return ans
            

