class Node:
    def __init__(self, value):
        self.value = value        # The value of the current node
        self.left = None          # Left child
        self.right = None         # Right child

# Create nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)


"""     10
       /  \
      5    15
     / \   / \
    2   7 12 20
 """