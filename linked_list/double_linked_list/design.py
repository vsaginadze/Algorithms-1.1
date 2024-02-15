class DoublyListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head):
        self.head = head
    
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
        self.head.prev = node
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

        idx, cur_node = 1, self.head.next
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




n3 = DoublyListNode(3)
n2 = DoublyListNode(2, n3)
n1 = DoublyListNode(1, n2)
head = DoublyListNode(0, n1)

n3.prev = n2
n2.prev = n1
n1.prev = head

    
doubly_list = DoublyLinkedList(head)

doubly_list.addAtHead(-1)
doubly_list.addAtTail(4)
doubly_list.addAtIndex(-1, 99)
doubly_list.display()