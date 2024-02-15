class DoublyListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.prev = None

n3 = DoublyListNode(3)
n2 = DoublyListNode(2, n3)
n1 = DoublyListNode(1, n2)
head = DoublyListNode(0, n1)

n3.prev = n2
n2.prev = n1
n1.prev = head



def display(head):
    if head:
        print(f'None <- {head.val} -> ', end="")

        cur_node = head.next

        while cur_node:
            print(f"<- {cur_node.val} -> ", end="")
            cur_node = cur_node.next
        print("None")
        
display(head)
