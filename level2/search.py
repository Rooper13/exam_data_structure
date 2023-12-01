class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search_node(root, value):
    if root is None or root.val == value:
        return root
    if root.val < value:
        return search_node(root.right, value)
    return search_node(root.left, value)

# Usage:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

value_to_search = 7  # Change this value to search for a different node
result = search_node(root, value_to_search)

if result:
    print(f"Found node with value {value_to_search}")
else:
    print(f"Node with value {value_to_search} not found")
