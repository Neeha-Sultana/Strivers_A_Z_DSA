'''
def areIsomorphic(str1: str, str2: str) -> bool:
    dict1 = {}
    dict2 = {}
    l1 = len(str1)
    l2 = len(str2)
    if l1 != l2:
        return False
    for i in range(l1):
        if str1[i] in dict1:
            if dict1[str1[i]] != str2[i]:
                return False
        else:
            dict1[str1[i]] = str2[i]

        if str2[i] in dict2:
            if dict2[str2[i]] != str1[i]:
                return False
        else:
            dict2[str2[i]] = str1[i]

    return True
'''

def areIsomorphic(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    
    mapping1 = {}
    mapping2 = {}
    mapped_chars1 = set()
    mapped_chars2 = set()
    
    for c1, c2 in zip(str1, str2):
        if c1 in mapping1:
            if mapping1[c1] != c2:
                return False
        elif c2 in mapping2:
            if mapping2[c2] != c1:
                return False
        elif c1 in mapped_chars1 or c2 in mapped_chars2:
            return False
        else:
            mapping1[c1] = c2
            mapping2[c2] = c1
            mapped_chars1.add(c1)
            mapped_chars2.add(c2)
    
    return True

