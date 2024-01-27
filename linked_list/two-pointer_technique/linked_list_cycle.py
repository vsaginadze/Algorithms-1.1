from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        if not head.next:
            if head.next != head: return False
        if not head.next.next: return False
        
        slow = head
        fast = slow.next

        
        while slow != fast:
            if fast is None or fast.next is None: return False
            fast = fast.next.next
            slow = slow.next
        
        return True