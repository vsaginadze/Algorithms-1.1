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

def display(head):
        if head is None: 
            print("None")
            return
        
        current = head
        while current.next:
            print(current.val, end=" -> ")
            current = current.next
        print(current.val)

# lst = ListNode(5, ListNode(6, ListNode(7, ListNode(8))))
lst = ListNode(1, ListNode(2))
n = 2
display(lst)

sol = Solution()
head = sol.removeNthFromEnd(lst, n)

display(head)


