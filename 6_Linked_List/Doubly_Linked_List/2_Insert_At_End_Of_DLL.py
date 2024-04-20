class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# Please do not change code above.

'''
def insertAtTail(head: Node, k: int) -> Node:
    # Write your code here
    temp=head
    new=Node(k)
    if head==None:
        return new
    while(temp.next!=None):
        temp=temp.next
    temp.next=new
    temp.prev=temp
    return head
'''

def insertAtTail(head: Node, k: int) -> Node:
    # Write your code here
    if head is None:
        newNode=Node(k)
        head=newNode
    else:
        temp=head
        while temp.next:
            temp=temp.next

        newNode=Node(k)
        temp.next=newNode
        newNode.prev=temp
    return head
