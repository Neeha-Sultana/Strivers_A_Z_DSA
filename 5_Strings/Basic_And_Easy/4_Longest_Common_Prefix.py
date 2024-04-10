'''
from typing import List
def commonPrefix(arr: List[str], n: int) -> str:
    if not arr:
        return "-1"
    prefix = arr[0]
    for i in range(len(prefix)):
        for string in arr[1:]:
            if i >= len(string) or string[i] != prefix[i]:
                return prefix[:i] if i > 0 else "-1"
    return prefix
 '''

from typing import List
def commonPrefix(arr: List[str], n: int) -> str:
    arr.sort()
    fir=arr[0]
    las=arr[-1]
    pre=''
    for i in range(len(fir)):
        if fir[i]!=las[i]:
            break

        pre=pre+fir[i]
    if pre=='' :
        return -1
    else :
        return pre
