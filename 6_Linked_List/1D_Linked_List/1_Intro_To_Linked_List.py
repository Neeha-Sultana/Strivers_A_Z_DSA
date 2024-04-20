class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def constructLL(arr:[int])->Node:
    if not arr:
        return None
    head=Node(arr[0])
    temp=head
    for i in range(1,len(arr)):
        newNode=Node(arr[i])
        temp.next=newNode
        temp=newNode

    return head


