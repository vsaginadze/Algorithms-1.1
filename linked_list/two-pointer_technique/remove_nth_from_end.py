from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def __len__(self, headL):
        node = headL
        size = 0

        while node:
            node = node.next
            size += 1

        return size

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = ListNode(None, head)
        length = self.__len__(a)

        if n == 1 == length: return None 
        
        removeAt = length - n
        if removeAt > 0:
            cnt = 1
            node = a
            while node:
                if cnt == removeAt:
                    node.next = node.next.next
                    break
                node = node.next
                cnt += 1
        
        return a.next



