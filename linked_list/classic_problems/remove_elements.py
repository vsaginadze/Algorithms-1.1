from typing import Optional
from linked_list import LinkedList, ListNode

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head:
            node = head = ListNode(None, head)
            
            while node.next:
                while node.next.val == val:
                    if node.next.next is None: return
                    node.next = node.next.next
                node = node.next

            return head.next
        
        return None

arr = [2,2,2,2,2]

lst = LinkedList(arr)
lst.array_to_linked_list()
lst.head.display()

sol = Solution()
head = sol.removeElements(lst.head, 2)

head.display()
