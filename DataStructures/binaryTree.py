class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif (data > self.data):
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
    def printTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def inOrder(self):
        if root:
            if self.left:
                self.left.inOrder()
            print(self.data)
            if self.right:
                self.right.inOrder()

    def preOrder(self):
        if root:
            print(self.data)
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
    
    def postOrder(self, root):
        if root:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print(self.data)

root = Node(4)
root.insert(3)
root.insert(5)