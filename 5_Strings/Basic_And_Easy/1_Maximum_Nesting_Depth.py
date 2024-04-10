def maxDepth(s:str) -> int:
    # Write your code here.
    ct=0
    maxi=0
    for i in range(len(s)):
        if s[i]=='(':
            ct+=1
            maxi=max(ct,maxi)
        elif s[i]==')':
            ct-=1
    return maxi
