'''
def sortByFrequency(n: int, s: str) -> str:
    # Write your code here
    dict1={}
    for i in s:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    sorted(dict1)
    stt=''
    for i in dict1:
        x=dict1[i]
        for j in range(x):
            stt+=i
    return stt
'''
def sortByFrequency(n: int, s: str) -> str:
    # Write your code here
    dict={}
    for x in s:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1 
    tuples = sorted(dict.items(),key=lambda x:x[1],reverse=True)
    li=[x[0]*x[1] for x in tuples]
    return "".join(li)
print(sortByFrequency(10,'aBaAcabaBC'))
