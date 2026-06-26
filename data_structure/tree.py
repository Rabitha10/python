class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create nodes
root = Node("A")
root.left = Node("B")
root.right = Node("C")

print(root.data)
print(root.left.data)
print(root.right.data)