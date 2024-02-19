class Solution:
    def flatten(self, head):
        if head is None: return
        if head.child:
            next_node = head.next
            child_head = self.flatten(head.child)
            
            head.next = child_head
            child_head.prev = head
            while child_head.next:
                child_head = child_head.next
            child_head.next = next_node
            if next_node:
                next_node.prev = child_head

            head.child = None
            return head

        self.flatten(head.next)
        return head





