'''
def isAnagram(str1, str2):
    lst1 = []
    lst2 = []
    for x, y in zip(str1, str2):
        lst1.append(x)
        lst2.append(y)
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        return True
    else:
        return False
'''
def isAnagram(str1, str2):
    dict1 = {}
    for i in str1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    for j in str2:
        if j in dict1:
            dict1[j] -= 1
        else:
            # Character in str2 not present in str1
            return False

    for y in dict1:
        if dict1[y] != 0:
            return False
    return True

print(isAnagram('abac', 'bacag'))


