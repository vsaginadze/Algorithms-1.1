from typing import Optional
from linked_list import LinkedList, ListNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        if head.next:
            e = eHead = head.next
            oTail = head

            while e:
                o = e.next
                if o:
                    e.next = o.next
                    o.next = eHead
                    oTail.next = o
                    oTail = o

                e = e.next

        return head



arr = [2,1,3,5,6,4,7]
arr1 = [1,2,3,4,5, 6]
lst = LinkedList(arr1)
lst.array_to_linked_list()
head = lst.head

head.display()

sol = Solution()
head = sol.oddEvenList(head)

head.display()