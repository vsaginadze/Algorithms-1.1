from typing import Optional
from linked_list import LinkedList, ListNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass



arr = [2,1,3,5,6,4,7]
arr1 = [1,2,3,4]
lst = LinkedList(arr1)
lst.array_to_linked_list()
head = lst.head

head.display()

sol = Solution()
head = sol.oddEvenList(head)

head.display()