class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def display(self):
        current_node = self

        while current_node.next:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        
        print(current_node.val)