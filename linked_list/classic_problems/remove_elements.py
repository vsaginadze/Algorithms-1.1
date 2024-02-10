from typing import Optional
from linked_list import LinkedList, ListNode

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(None, head)
        
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            node = node.next
        
        return head

arr = [1,2,2,2,3,5]

lst = LinkedList(arr)
lst.array_to_linked_list()
lst.display()

sol = Solution()
head = sol.removeElements(lst.head, 2)

head.display()
