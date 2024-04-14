from sys import *
from collections import *
from math import *
'''
def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    a=[]
    for i in range(n):
        a.append(arr[i])
    
    for i in range(0,n):
        a[(i-1)%n]=arr[i]
    return a


def rotateArray(arr: [], n: int) -> []:
    x=arr[1:n]
    x.append(arr[0])
    return x

'''

def rotateArray(arr: [], n: int) -> []:
    x=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]

    arr[n-1]=x
    return arr
