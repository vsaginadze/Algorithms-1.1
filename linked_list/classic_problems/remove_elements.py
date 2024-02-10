from typing import Optional
from linked_list import ListNode

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head = ListNode(None, head)
        
        while node and node.next:
            while node.next.val == val:
                node.next = node.next.next
                if node.next is None: break
            node = node.next
        
        return head.next