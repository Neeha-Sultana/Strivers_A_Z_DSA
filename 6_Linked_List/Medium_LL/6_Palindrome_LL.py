# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stt=[]
        temp=head
        while temp:
            stt.append(temp.val)
            temp=temp.next
            
        xx=[]
        for i in range(len(stt)-1,-1,-1):
            xx.append(stt[i])
        #print(stt)
        #print(xx)
        if xx==stt:
            return True
        else:
            return False
        

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stt=[]
        temp=head
        while temp:
            stt.append(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if stt.pop()!=temp.val:
                return False
            temp=temp.next
        return True
"""      

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        midd=slow
        temp=slow
        while tt and tt.next:
            prev=None
            ff=tt.next
            tt.next=prev
