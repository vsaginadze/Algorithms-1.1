from typing import Optional
from linked_list import LinkedList,ListNode

class Solution:
    def __length__(self, headL):
        node, length = headL, 0
        while node:
            length += 1
            node = node.next
        
        return length
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            # if k is larger than length k % length
            size = self.__length__(head)
            k = k % size if k >= size else k
            if k == 0: return head
            if k == 1 and size == 1: return head
            # set slow and fast by k pointers apart
            slow = fast = head
            while fast and k+1:
                fast = fast.next
                k -= 1

            # move sublist after slow pointer before head
            while fast:
                slow = slow.next
                fast = fast.next

            xead = slow.next
            node = xead
            slow.next = None
            while node.next:
                node = node.next

            node.next = head
            return xead
        return None

arr = [1,2,3,4,5]

head = LinkedList(arr).head
head.display()

sol = Solution()
sol.rotateRight(head, 2).display()