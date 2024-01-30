from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __len__(self, headL):
        node = headL
        size = 0

        while node:
            node = node.next
            size += 1

        return size

class Solution:
    def __len__(self, headL):
        node = headL
        size = 0

        while node:
            node = node.next
            size += 1

        return size
    
    

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = head
        print(a.val)
        length = self.__len__(a)
        removeAt = length - n

        if removeAt > 0:
            cnt = 0
            node = a
            while node:
                if cnt == removeAt:
                    node.next = node.next.next
                    break
                node = node.next
        
        return a

def display(head):
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

lst = ListNode(5, ListNode(6, ListNode(7, ListNode(8))))
display(lst)

sol = Solution()
head = sol.removeNthFromEnd(lst, 2)

display(head)


