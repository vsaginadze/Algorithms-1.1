from typing import Optional

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            if head.next == head: return head
            if head.next.next == head 
            slow = head
            fast = slow
            
            while slow is not fast:
                if fast is None or fast.next is None: return None
                
                fast = fast.next.next
                slow = slow.next
            
            return slow
        
        return None

# tail = ListNode(4)
# n3 = ListNode(0, tail)
# n2 = ListNode(2, n3)
# head = ListNode(3, n2)

# tail.next = n2

# sol = Solution()
# print(sol.detectCycle(head))