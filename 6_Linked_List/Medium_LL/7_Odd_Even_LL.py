class Solution:
	def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

		if head == None:
			return None

		odd_node = head
		even_node = head.next
		evenhead = head.next

		while even_node != None and even_node.next != None:
			odd_node.next = odd_node.next.next
			even_node.next = even_node.next.next

			odd_node = odd_node.next
			even_node = even_node.next

		odd_node.next = evenhead

		return head
    
