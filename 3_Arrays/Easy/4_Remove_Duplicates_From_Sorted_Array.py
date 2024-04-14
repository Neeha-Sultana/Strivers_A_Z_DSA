def dup(arr):
    ct=0
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            ct+=1

        else:
            continue

    return ct+1

print(dup([3,4,5,6,6,454,454]))
