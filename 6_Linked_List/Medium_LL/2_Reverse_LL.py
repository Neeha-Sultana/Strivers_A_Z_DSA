# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stacc=[]
        temp=head
        ct=0
        while temp:
            stacc.append(temp.val)
            temp=temp.next
            ct+=1
        temp=head
        for i in range(ct):
            temp.val=stacc.pop()
            temp=temp.next
            
        return head
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=None
        while temp:
            front=temp.next  
            temp.next=prev
            prev=temp
            temp=front
            
        return prev
