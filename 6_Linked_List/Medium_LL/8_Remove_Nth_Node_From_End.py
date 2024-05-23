
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        tail=dummy
        nnn=dummy
        
        for i in range(n):
            tail=tail.next
            
        while (tail.next is not None):
            tail=tail.next
            nnn=nnn.next
            
        nnn.next=nnn.next.next
        
        return dummy.next    
'''        

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        ct = 1
        if head is None or (head.next is None and n == 1):
            return None
        while temp.next is not None:
            ct += 1
            temp = temp.next
        if ct == n:
            return head.next
        xx = ct - n
        temp = head
        for i in range(1, xx):
            temp = temp.next
        temp.next = temp.next.next
        return head
