from typing import Optional
from linked_list import LinkedList, ListNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        node = head.next.next
        idx = 3

        while node:
            if idx % 2 == 0:
                pass
            else:
                odd.next = node
            node = node.next
            idx += 1
        
        return head


arr = [2,1,3,5,6,4,7]
arr1 = [1,2,3,4]
lst = LinkedList(arr1)
lst.array_to_linked_list()
head = lst.head

head.display()

sol = Solution()
head = sol.oddEvenList(head)

head.display()