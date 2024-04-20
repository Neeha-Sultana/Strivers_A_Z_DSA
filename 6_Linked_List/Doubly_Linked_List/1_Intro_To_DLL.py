class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def constructDLL(arr: [int]) -> Node:
    head=Node(arr[0])
    temp=head
    prev=None
    for i in range(1,len(arr)):
        newNode=Node(arr[i])
        temp.next=newNode
        temp=temp.next
        prev=Node(arr[i-1])

    return head
