class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

class LinkedList:
    def __init__(self, arr=[]):
        self.head = None
        self.arr = arr

    def display(self):
        current_node = self.head

        while current_node.next:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        
        print(current_node.val)

    def array_to_linked_list(self):
        if not self.arr:
            return None
        
        self.head = ListNode(self.arr[0])
        current_node = self.head

        for value in self.arr[1:]:
            current_node.next = ListNode(value)
            current_node = current_node.next
        
        return self.head