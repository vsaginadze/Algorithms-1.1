from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        len_a = 0
        len_b = 0

        p = a
        while p:
            len_a += 1
            p = p.next

        p = b
        while p:
            len_b += 1
            p = p.next
        
        if len_a > len_b:
            skip = len_a - len_b

            a = headA
            cnt = 0
            while a:
                if cnt == skip:
                    break
                a = a.next
                cnt += 1

            b = headB

            while a.val != b.val:
                a = a.next
                b = b.next
            
            if a.next == None and b.next == None:
                return None
            else:
                return a.val
        
        else:
            skip = len_b - len_a

            b = headB
            cnt = 0
            while b:
                if cnt == skip:
                    break
                b = b.next
                cnt += 1
            
            a = headA

            while a.next != b.next:
                a = a.next
                b = b.next
            
            if a.next == None and b.next == None:
                return None
            else:
                return a.val
                

def list_to_linked_list(lst):
    # Initialize the head of the linked list
    head = None
    # Iterate through the list in reverse order to efficiently build the linked list
    for val in reversed(lst):
        # Create a new node with the current value and link it to the current head
        head = ListNode(val, head)
    return head

def display(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

a = [4,4,5]
b = [5,6,1,12,4,5]

linked_a = list_to_linked_list(a)
linked_b = list_to_linked_list(b)

sol = Solution()
print(sol.getIntersectionNode(linked_a, linked_b))