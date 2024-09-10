
class Tree:
    def __init__(self):
        self.root = None
    # first implementation: wrong
    # not changing the state of the problem size when recursing, creating unlimited recursion
    def wrongbalancedBST(self, arr):
        mid = len(arr)//2
        if len(arr) == 1:
            return Node(arr[mid])
        root = Node(arr[mid])
        self.wrongBSThelper(root, mid, arr)
        return root.data, root.left, root.right

    def wrongBSThelper(self, root, mid, arr):
        if mid < 0 or mid >= len(arr):
            return 
        if mid - 1 >= 0:
            root.left = Node(arr[mid-1])
            self.BSThelper(root.left, mid-1, arr)

        if mid + 1 < len(arr):
            root.right = Node(arr[mid+1])
            self.BSThelper(root.right, mid+1, arr)
        
    # correct implementation: working on smaller segment sizes each recurse
    def BST(self, arr):
        if not arr:
            return
        return self.BSThelper(arr)
    
    def BSThelper(self, arr):
        if not arr:
            return None
        mid = len(arr)//2
        root = Node(arr[mid])
        root.left = self.BSThelper(arr[:mid])
        root.right = self.BSThelper(arr[mid+1:]) # without middle 

        return root
    # Time: O(n log n)
    # Space: O(n)
    

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example usage:
arr = [40, 60, 100, 103, 704]
t = Tree()
root = t.BST(arr)

def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.data, end=' ')
    inorder_traversal(node.right)

inorder_traversal(root)