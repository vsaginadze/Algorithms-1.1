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

    def move_pointer_by(self, diff, headL):
        cnt = 0
        node = headL
        
        while node:
            if cnt == diff: break
            node = node.next
            cnt += 1
        
        return node

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        sizeA = self.__len__(a)
        sizeB = self.__len__(b)
        diff = abs(sizeA - sizeB)

        if sizeA > sizeB:
            a = self.move_pointer_by(diff, a)
        else:
            b = self.move_pointer_by(diff, b)
        
        while a and b:
            if a is b: return a
            a, b = a.next, b.next
