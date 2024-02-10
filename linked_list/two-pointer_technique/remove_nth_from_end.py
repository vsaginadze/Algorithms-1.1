from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def display(self):
        current_node = self

        while current_node.next:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        
        print(current_node.val)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n > 0:
            head = ListNode(None, head)
            slow = fast = head

            for i in range(n):
                if fast and fast.next: 
                    fast = fast.next
                else:
                    return None

            while fast.next:
                fast = fast.next
                slow = slow.next

            slow.next = slow.next.next

            return head.next
        
        return None

# n2 = ListNode(3, ListNode(4, ListNode(6, ListNode(5))))
n1 = ListNode(2, None)
head = ListNode(1, n1)

head.display()

sol = Solution()
head = sol.removeNthFromEnd(head, 3).display()
