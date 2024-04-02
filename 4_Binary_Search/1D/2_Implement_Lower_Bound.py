'''
#Bruteforce approach
def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(n):
        if arr[i] >= x:
            #lower bound found
            return i
    return n
'''


#Optimal
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    low=0
    ans=n
    high=len(arr)-1
    while (low<=high):
        midd=(low+high)//2
        if arr[midd]>=x:
            ans=midd
            high=midd-1
        else:
            low=midd+1
    return ans

