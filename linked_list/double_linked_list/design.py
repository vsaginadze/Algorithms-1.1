class DoublyListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self) -> None:
        if self.head:
            print(f'None <- ({self.head.val}) -> ', end="")

            cur_node = self.head.next

            while cur_node:
                print(f"<- ({cur_node.val}) -> ", end="")
                cur_node = cur_node.next
            print("None")
    
    def addAtHead(self, val) -> None:
        node = DoublyListNode(val, self.head)
        if self.head:
            self.head.prev = node
            self.head = node
        else:
            self.head = node
    
    def addAtTail(self, val) -> None:
        node = DoublyListNode(val)
        if self.head:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            
            cur_node.next = node
            node.prev = cur_node
        else:
            self.head = node
    
    def get(self, index: int) -> int:
        if not index >= 0: return -1
        idx, current_node = 0, self.head
        while current_node:
            if idx == index:
                return current_node.val
            current_node = current_node.next
            idx += 1
        
        return -1

    def addAtIndex(self, index: int, val: int) -> None:
        if not index >= 0: return

        idx, cur_node = 0, self.head
        node = DoublyListNode(val)
        if index:
            while cur_node:
                if idx == index:
                    node.next = cur_node
                    node.prev = cur_node.prev
                    cur_node.prev.next = node
                    cur_node.prev = node
                idx += 1
                cur_node = cur_node.next
        else:
            self.addAtHead(val)
    
    def deleteAtIndex(self, index: int) -> None:
        if not index >= 0: return
        idx, current_node = 1, self.head
        if index:
            while current_node.next:
                current_node = current_node.next
                if idx == index:
                    current_node.prev.next = current_node.next
                    return
                idx += 1
        else:
            self.head = self.head.next

