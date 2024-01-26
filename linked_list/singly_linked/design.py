class MyLinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def display(self):
        current_node = self.head

        while current_node.next is not None:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        
        print(current_node.val)

    def get(self, index: int) -> int:
        idx, current_node = 0, self.head
        
        while current_node is not None:
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
        if self.head is None:
            self.head = node
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next
        
            current_node.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        idx, current_node = 0, self.head
        node = self.Node(val, None)
        if idx == index:
            node.next = self.head
            self.head = node
            return
        
        idx = 1
        while current_node is not None:
            prev_node = current_node
            current_node = current_node.next
            if idx == index:
                prev_node.next = node
                node.next = current_node
                break
            idx += 1

    def deleteAtIndex(self, index: int) -> None:
        idx, current_node = 0, self.head
        if idx == index:
            self.head = self.head.next
            return
        
        idx = 1
        while current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next
            if idx == index:
                prev_node.next = current_node.next
                break
            idx += 1