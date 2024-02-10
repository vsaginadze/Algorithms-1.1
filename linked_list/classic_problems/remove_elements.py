from typing import Optional
from linked_list import LinkedList, ListNode

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head = ListNode(None, head)
        
        while node and node.next:
            while node.next.val == val:
                node.next = node.next.next
                if node.next is None: break
            node = node.next
        
        return head.next

arr = [2,1,2]
target = 2

lst = LinkedList(arr)
lst.array_to_linked_list()
lst.head.display()

sol = Solution()
head = sol.removeElements(lst.head, target)

if not head: 
    print("[]")
else:
    head.display()
