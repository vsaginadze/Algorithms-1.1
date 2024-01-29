from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            slow = fast = head

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                
                if slow == fast:
                    slow = head

                    while slow != fast:
                        slow = slow.next
                        fast = fast.next

                    return slow
        
        return None