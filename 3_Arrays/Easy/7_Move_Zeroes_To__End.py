'''
def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    ct=0
    for i in range(n-1,-1,-1):
        if a[i]==0:
            ct+=1
            a.pop(i)

    for i in range(ct):
        a.append(0)
    return a
'''


def moveZeros(n: int,  a: [int]) -> [int]:
    l = 0
    for r in range(len(a)):
        if a[r]!=0:
            a[l], a[r] = a[r], a[l]
            l += 1
    return a
