""" -----------------------------------------------------------------------
    breadth-first search (BFS) and depth-first search (DFS) implementation 
 ------------------------------------------------------------------------- """
from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def BFS(self, root):
        if root is None:
            return
        
        queue = deque([root])

        while queue:
            node = queue.popleft() # dequeue a node from the front of the queue
            print(node.value, end = ' ') # visit the node (print its value in this case)

            # enqueue left child
            if node.left:
                queue.append(node.left)
            # enqueue right child
            if node.right:
                queue.append(node.right)
    
    def DFS(self,node):
        if node is None:
            return
        # print the node's value
        print(node.value, end=' ')

        # recursively call DFS on left child
        self.DFS(node.left)
        # recursively call DFS on right child
        self.DFS(node.right)

rootbfs = Node(1)
rootbfs.left = Node(2)
rootbfs.right = Node(3)
rootbfs.left.left = Node(4)
rootbfs.right.right = Node(5)

rootbfs.BFS(rootbfs)
# Expected [1, 2, 3, 4, 5]

print('\n')

rootdfs = Node(1)
rootdfs.left = Node(2)
rootdfs.right = Node(3)
rootdfs.left.left = Node(4)
rootdfs.right.right = Node(5)

rootdfs.DFS(rootdfs)
# Expected [1, 2, 4, 3, 5]