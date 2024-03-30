"""
#Bruteforce
def lar(arr):
    for i in range(len(arr)):
        sm=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[sm]:
                sm=j
        arr[i],arr[sm]=arr[sm],arr[i]
    return arr[-1]
"""
#Optimal
def lar(arr):
    lar=arr[0]
    for i in range(len(arr)):
        if arr[i]>lar:
            lar=arr[i]

    return lar


print(lar([23,43,12,4,22,123,35,2]))
