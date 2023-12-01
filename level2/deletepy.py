class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

def display_tree(root):
    if root:
        display_tree(root.left)
        print(root.val, end=" ")
        display_tree(root.right)

def deleteNode(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root

# Usage:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print("Binary Search Tree before deletion:")
display_tree(root)
print()

root = deleteNode(root, 12)

print("Binary Search Tree after deletion of node with value 12:")
display_tree(root)
