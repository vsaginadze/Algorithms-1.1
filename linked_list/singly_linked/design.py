class MyLinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def display(self):
        current_node = self.head

        while current_node.next:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        
        print(current_node.val)

    def get(self, index: int) -> int:
        idx, current_node = 0, self.head
        
        while current_node:
            if idx == index:
                return current_node.val
            current_node = current_node.next
            idx += 1
        
        return -1

    def addAtHead(self, val: int) -> None:
        node = self.Node(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = self.Node(val)
        if self.head:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
        
            current_node.next = node
        else:
            self.head = node

    def addAtIndex(self, index: int, val: int) -> None:
        if not index >= 0: return

        idx, current_node = 1, self.head
        node = self.Node(val, None)
        if index:
            while current_node:
                prev_node = current_node
                current_node = current_node.next

                if idx == index:
                    prev_node.next = node
                    node.next = current_node
                    break

                idx += 1
        else:
            node.next = self.head
            self.head = node

    def deleteAtIndex(self, index: int) -> None:
        if not index >= 0: return

        idx, current_node = 1, self.head
        if index:
            while current_node.next:
                prev_node = current_node
                current_node = current_node.next

                if idx == index:
                    prev_node.next = current_node.next
                    return
                
                idx += 1
        else:
            self.head = self.head.next