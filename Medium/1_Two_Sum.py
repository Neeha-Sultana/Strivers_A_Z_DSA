def twosum(arr,tar):
    n=len(arr)
    for i in range(len(arr)):
        summ=0
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==tar:
                return True

    return False

print(twosum([2,6,5,8,11],15))
