class DoublyListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head):
        self.head = head
    
    def display(self):
        if self.head:
            print(f'None <- ({self.head.val}) -> ', end="")

            cur_node = self.head.next

            while cur_node:
                print(f"<- ({cur_node.val}) -> ", end="")
                cur_node = cur_node.next
            print("None")
    
    def addAtHead(self, val):
        node = DoublyListNode(val, self.head)
        self.head.prev = node
        self.head = node

n3 = DoublyListNode(3)
n2 = DoublyListNode(2, n3)
n1 = DoublyListNode(1, n2)
head = DoublyListNode(0, n1)

n3.prev = n2
n2.prev = n1
n1.prev = head

    
doubly_list = DoublyLinkedList(head)

doubly_list.addAtHead(-1)
doubly_list.display()