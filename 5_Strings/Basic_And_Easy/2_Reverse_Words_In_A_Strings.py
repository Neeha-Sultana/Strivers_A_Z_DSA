'''
def reverseString(s: str) -> str:
    words = s.split()  
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string



def reverseString(s: str) -> str:
    stack = []
    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            stack.append(word)
            word = ""
    stack.append(word)  # Add the last word

    reversed_string = ""
    while stack:
        reversed_string += stack.pop() + " "

    
    return reversed_string[:-1]
'''

def reverseString(s: str) -> str:
    left = 0
    right = len(s) - 1
    
    temp = ""
    ans = ""

    while left <= right:
        ch = s[left]
        if ch != ' ':
            temp += ch
        elif ch == ' ':
            if ans != "":
                ans = temp + " " + ans
            else:
                ans = temp
            temp = ""
        left += 1
    
    # If not empty string then add to the result(Last word is added)
    if temp != "":
        if ans != "":
            ans = temp + " " + ans
        else:
            ans = temp
    
    return ans

