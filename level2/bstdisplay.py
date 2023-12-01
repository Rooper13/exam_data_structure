class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def display_tree(root):
    if root:
        display_tree(root.left)
        print(root.val, end=" ")
        display_tree(root.right)

# Usage:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print("Binary Search Tree:")
display_tree(root)
