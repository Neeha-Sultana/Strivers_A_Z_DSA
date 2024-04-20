'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def searchInLinkedList(head, k):
    # Your code goes here.
    temp=head
    while temp:
        if temp.data!=k:
            temp=temp.next
        else:
            return 1

    return 0
