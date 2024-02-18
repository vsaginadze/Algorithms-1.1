from typing import Optional
from linked_list import ListNode, LinkedList

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode(None, None)
        node = sorted_list

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next
        
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        
        return sorted_list.next
        


list1 = [0,2,5]
list2 = [1,3,4]

lst1 = LinkedList(list1)
lst2 = LinkedList(list2)

lst1.display()
lst2.display()

sol = Solution()
sorted_lst = sol.mergeTwoLists(lst1.head, lst2.head)
sorted_lst.display()