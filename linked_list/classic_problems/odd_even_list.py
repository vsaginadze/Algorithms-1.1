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