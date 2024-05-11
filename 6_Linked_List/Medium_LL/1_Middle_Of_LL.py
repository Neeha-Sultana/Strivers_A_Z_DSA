# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        countt=0
        while temp is not None:
            temp=temp.next
            countt+=1
        mi=((countt//2)+1)
        temp=head
        i=1
        
        while (i<mi):
            temp=temp.next
            i=i+1
        return temp
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow
        
