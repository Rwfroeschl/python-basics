class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        # bad implementation
        self.mini = {}
        # good implementation
        self.min_stack = None

    def push(self, item):
        # bad implementation
        self.mini[item] = 1
        # good implementation
        if not self.min_stack or item <= self.min_stack.data:
            new_min = StackNode(item)
            new_min.next = self.min_stack
            self.min_stack = new_min
        new_node = StackNode(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            # bad implementation
            del self.mini[self.head.data]
            # good implementation
            if self.head.data == self.min_stack.data:
                self.min_stack = self.min_stack.next
            self.head = self.head.next
        else:
            raise Exception("Can not pop an empty stack")
        
    def peek(self):
        if self.head:
            return (self.head.data)
        else:
            raise Exception("Can not peek an empty stack")
        
    # bad implementation
    def minimum(self):
        if self.head:
            return min(self.mini, key=self.mini.get)
        else:
            raise Exception("Empty stack")
    # good implementation
    def get_min(self):
        if self.min_stack:
            return self.min_stack.data
        else:
            raise Exception("Nothing in stack")
        
    # time: O(n) / incorrect, needs to be O(1)
    # spcae: O(n)
        


ss = Stack()
ss.push(1)
print(ss.peek())
ss.push(4)
print(ss.peek())
ss.push(5)
print(ss.peek())
print(ss.mini)
ss.pop()
print("first pop: ",ss.peek())
ss.pop()
print("second pop: ",ss.peek())
print(ss.mini)
ss.push(0)
ss.pop()
print("third pop: ",ss.peek())

print("O(n) time: ", ss.minimum())
print("O(1) time: ", ss.get_min())


