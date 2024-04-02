#Bruteforce
"""
def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    for i in range(n):
        if arr[i]>x:
            return i
    return n
"""
#Optimal
def upperBound(arr: [int], x: int, n: int) -> int:
    low=0
    high=n-1
    ans=n
    while(low<=high):
        midd=(low+high)//2
        if arr[midd]>x:
            ans=midd
            high=midd-1
        else:
            low=midd+1
    return ans
