from typing import Optional
from linked_list import ListNode, LinkedList

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_head = ListNode(None)
        current_node = number_head
        add_one = False

        while l1 and l2:
            sum_of_two = 0
            if add_one: 
                sum_of_two += 1
                add_one = False
            
            sum_of_two += l1.val+l2.val

            if sum_of_two >= 10:
                sum_of_two = sum_of_two % 10
                add_one = True
            
            current_node.next = ListNode(sum_of_two)
            current_node = current_node.next
            l1 = l1.next
            l2 = l2.next

        if not l1:
            node = l2
        elif not l2:
            node = l1

        if add_one:
            while node and add_one:
                if node.val+1 == 10:
                    current_node.next = ListNode(0)
                    current_node = current_node.next
                    node = node.next
                else:
                    current_node.next = ListNode(node.val+1, node.next)
                    add_one = False
        else:
            current_node.next = node

        if add_one: current_node.next = ListNode(1)

        return number_head.next


l1 = [9,9,1]
l2 = [1]

lst1 = LinkedList(l1)
lst2 = LinkedList(l2)

lst1.display()
lst2.display()

sol = Solution()
sum_of_two = sol.addTwoNumbers(lst1.head, lst2.head)
sum_of_two.display()