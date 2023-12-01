class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, key):
        if key < self.val:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        elif key > self.val:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)

def display_tree(root):
    if root:
        display_tree(root.left)
        print(root.val, end=" ")
        display_tree(root.right)

# Usage:
# Existing tree
root = Node(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(7)
root.insert(12)
root.insert(20)

print("Binary Search Tree before insertion of 8:")
display_tree(root)

# Inserting a new node with value 8
root.insert(8)

print("\nBinary Search Tree after insertion of 8:")
display_tree(root)
