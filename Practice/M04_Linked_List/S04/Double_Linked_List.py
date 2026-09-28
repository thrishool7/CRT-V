class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList: 
    def __init__(self):
        self.head = None
DoublyLinkedList = DoublyLinkedList()
DoublyLinkedList.head = Node(10)

class Double_LL:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def insert_at_position(self, data, position):
        if position < 1:
            print("Position should be >= 1.")
            return
        new_node = Node(data)
        if position == 1:
            self.insert_at_beginning(data)
            return
        current = self.head
        for _ in range(position - 2):
            if current is None:
                print("Position is greater than the number of nodes.")
                return
            current = current.next
        if current is None:
            print("Position is greater than the number of nodes.")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None
