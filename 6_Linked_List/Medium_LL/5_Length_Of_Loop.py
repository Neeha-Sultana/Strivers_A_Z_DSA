def countNodesinLoop(head):
    if not head or not head.next:
        return 0
    
    # Function to detect the loop and return the meeting point
    def detectLoop(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
    
    # Detect the loop
    meeting_point = detectLoop(head)
    if not meeting_point:
        return 0
    
    # Count the number of nodes in the loop
    count = 1
    temp = meeting_point.next
    while temp != meeting_point:
        count += 1
        temp = temp.next
        
    return count
