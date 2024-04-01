'''
#Bruteforce
def sec_lar(arr):
    for i in range(len(arr)):
        sm=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[sm]:
                sm=j
        arr[i],arr[sm]=arr[sm],arr[i]

    for i in range(len(arr)-1,0,-1):
        if arr[i]!=arr[-1]:
            return arr[i]
        
   
print(sec_lar([23,34,22,1,344,65,4]))

#Better
def sec_lar(arr):
    lar=-1
    for i in range(len(arr)):
        if arr[i]>lar:
            lar=arr[i]
    seclar=-1
    for i in range(len(arr)):
        if arr[i]<lar and arr[i]>seclar:
            seclar=arr[i]
    return seclar
print(sec_lar([34343,23,34,22,1,344,65,4]))
'''

#Optimal
def sec_lar(arr):
    lar = arr[0]
    seclar = float('-inf')  # Initialize second largest to negative infinity
    for i in range(1, len(arr)):
        if arr[i] > lar:
            seclar = lar
            lar = arr[i]
        elif arr[i] > seclar and arr[i] != lar:
            seclar = arr[i]
    return seclar

print(sec_lar([34343, 23, 34, 22, 1, 344, 65, 4]))

