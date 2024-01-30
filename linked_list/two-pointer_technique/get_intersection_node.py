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

    def set_pointer_forward(self, headL, diff):
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
            a = self.set_pointer_forward(a, diff)
        else:
            b = self.set_pointer_forward(b, diff)
        
        while a and b:
            if a is b: return a
            a = a.next
            b = b.next
        
        
                
a1 = ListNode(1)
headA = ListNode(4, a1)

b2 = ListNode(1)
b1 = ListNode(6, b2)
headB = ListNode(5, b1)

rest = ListNode(8, ListNode(4, ListNode(5)))

a1.next = rest
b2.next = rest

sol = Solution()
print(sol.getIntersectionNode(headA, headB))
