class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node:
    # Write your code here
    temp=head
    if head.next is None:
        return None

    while temp.next:
        temp=temp.next


    temp=temp.prev
    temp.next=None
    temp.prev=None

    return head
