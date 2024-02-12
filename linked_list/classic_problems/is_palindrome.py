from typing import Optional
from linked_list import LinkedList, ListNode

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return None
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        
        return arr == arr[::-1]

arr = [1,2,2,1]
arr1 = [1,2,2,3,2,1]
lst = LinkedList(arr)
lst.array_to_linked_list()
head = lst.head

head.display()

sol = Solution()
# head = sol.oddEvenList(head)

head.display()