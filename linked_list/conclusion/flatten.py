class Solution:
    def flatten(self, head):
        if head is None:
            return
        if head.child:
            next_node = head.next
            childHead = self.flatten(head.child)
            
            head.next = childHead
            childHead.prev = head
            while childHead.next:
                childHead = childHead.next
            childHead.next = next_node
            if next_node:
                next_node.prev = childHead

            head.child = None
            return head

        self.flatten(head.next)
        return head





