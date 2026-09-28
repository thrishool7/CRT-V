'''
Double Linked List:
The data can be stored in the nodes
Nodes -> prev | data | next 
Algorithm:
1. Creating Nodes
2. Insert the data
3. Connection btw the nodes
4. Traverse each node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

node2.prev = node1
node3.prev = node2
node4.prev = node3

def traverse_forward():
    curr = node1
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")
traverse_forward()

def traverse_backward():
    curr = node4
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.prev
    print("None")
traverse_backward()


#insertion at the beginning:
def insert_begin(self, data):
    self.head = data
    self.next = node1
    self.prev = None
def insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node
def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)
traverse(head)
print()

