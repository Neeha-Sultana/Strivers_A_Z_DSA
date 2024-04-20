'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    #Your code goes here
    temp=head
    ct=0
    while(temp):
        ct+=1
        temp=temp.next
    return ct
