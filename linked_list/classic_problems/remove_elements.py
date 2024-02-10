from typing import Optional
from linked_list import LinkedList, ListNode

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        
        while node:
            if node.val == val:
                pass