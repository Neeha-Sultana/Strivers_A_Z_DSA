'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    # Write your code here
    if head is None or head.next is None:
        return head
    else:
        arr=[]
        temp=head

        while temp:
            arr.append(temp.data)
            temp=temp.next


        temp=head
        while temp:
            temp.data=arr.pop()
            temp=temp.next
    return head
