from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def display(self):
        current_node = self

        while current_node.next:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        
        print(current_node.val)

class Solution:
    def pluck_even_nodes(self, head):
        even_head = Node(-1)  # Creating a dummy head for the even nodes
        even_node = even_head
        current = head
        index = 0

        while current:
            if index % 2 == 1:  # If index is even (zero-based indexing)
                even_node.next = current
                even_node = even_node.next
                prev_next = current.next
                current.next = None
                current = prev_next
            else:
                current = current.next
            index += 1

        return even_head.next  # Return the head of even nodes
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        xead = head
        node = xead

        while node:
            next = node.next
            node.next = Node(node.val, node.next)
            node = next

        node = xead
        while node:
            if node.random:
                node.next.random = node.random.next

            node = node.next.next

        
        return self.pluck_even_nodes(xead)

n4 = Node(1)
n3 = Node(10, n4)
n2 = Node(11, n3)
n1 = Node(13, n2)
head = Node(7, n1)

n1.random = head
n2.random = n4
n3.random = n3
n4.random = head

head.display()

sol = Solution()
new_head = sol.copyRandomList(head)
new_head.display()
