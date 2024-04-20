class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Please do not change code above.


def deleteLast(list: Node) -> Node:
    # Write your code here
    head=list
    temp=list
    prev=0
    while temp.next is not None:
        prev=temp
        temp=temp.next
    prev.next=0
    return head
