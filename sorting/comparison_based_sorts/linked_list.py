class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            
        def display(self):
            current_node = self

            while current_node.next:
                print(current_node.val, end=" -> ")
                current_node = current_node.next
            
            print(current_node.val)

class LinkedList:
    def __init__(self, arr=[]):
        self.head = None
        self.arr = arr

        self.array_to_linked_list()

    def array_to_linked_list(self):
        if not self.arr:
            return None
        
        self.head = ListNode(self.arr[0])
        current_node = self.head

        for value in self.arr[1:]:
            current_node.next = ListNode(value)
            current_node = current_node.next
        
        

    def display(self):
        current_node = self.head

        while current_node.next:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        
        print(current_node.val)