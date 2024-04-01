'''
#Better
def sorte(arr):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True
'''
#Optimal
def sorte(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


print(sorte([3,4,23,123,344]))
