from typing import Optional
from node import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            first_node = head

            while first_node.next:
                next_node = first_node.next
                first_node.next = next_node.next
                next_node.next = head
                head = next_node

            return head
        
        return None