
def rotateArray(arr: list, k: int) -> list:
    rev(arr,0,len(arr)-1)
    x=len(arr)-k
    rev(arr,0,x-1)
    rev(arr,x,len(arr)-1)
    return arr

def rev(arr,start,end):
    while(start<end):
        tempp=arr[start]
        arr[start]=arr[end]
        arr[end]=tempp
        start+=1
        end-=1
'''
def rotateArray(arr: list, k: int) -> list:
    n=len(arr)
    a=arr[k:]+arr[0:k]
    return a




def rotateArray(arr: list, k: int) -> list:
    a=[]
    for i in arr:
        a.append(i)
    for i in range(len(arr)):
        a[(i-k)%len(a)]=arr[i]
    return a



'''

