class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

class append():
    def __init__(self,val):    
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


# Create list and append values
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)