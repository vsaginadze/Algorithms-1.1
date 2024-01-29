from typing import Optional

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            slow = head.next
            fast = head.next.next
            
            while slow is not fast:
                fast = fast.next.next
                slow = slow.next

            slow = head
            
            while slow is not fast:
                fast = fast.next
                slow = slow.next
            
            print(slow.val)


tail = ListNode(4)
n3 = ListNode(0, tail)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
head = ListNode(3, n1)

tail.next = n2

sol = Solution()
sol.detectCycle(head)