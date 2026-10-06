class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Tree structure
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

#Tree Traversal ==> DFS(pre-order, in-order, post-order)
def pre_order(root):
    if root:
        print(root.data, end="-->")
        pre_order(root.left)
        pre_order(root.right)
print()
pre_order(root)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end="-->")
        in_order(root.right)
print()
in_order(root)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end="-->")
print()
post_order(root)


