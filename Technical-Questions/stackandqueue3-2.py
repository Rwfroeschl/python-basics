class Stack:
    def __init__(self):
        self.stack = []
        self.smallest = 0
        self.track = {}
    def push(self, item):
        if not self.stack:
            self.smallest = item
        elif item < self.smallest:
            self.smallest = item
        self.stack.append(item)
    def pop(self):
        print ("smallest and top of stack before pop", self.smallest, self.stack[-1])
        if self.smallest == self.stack[-1]:
            self.smallest = min(self.stack)
        if self.stack:
            self.stack.pop()
        else:
            raise Exception("Can not pop an empty stack")
    def peek(self):
        if self.stack:
            return print(self.stack[-1])
        else:
            raise Exception("Can not peek an empty stack")
        
    # returns minimum element
    def minimum(self):
        if self.stack:
            return min(self.stack)
        else:
            raise Exception("Empty stack")
        
    def mini(self):
        if self.stack:
            return self.smallest
        else:
            raise Exception("Empty stack")


ss = Stack()
ss.push(1)
ss.push(4)
ss.push(5)
ss.pop()
ss.pop()
ss.push(0)
ss.pop()
ss.peek()

print("minimum function: ",ss.minimum())
print("mini function: ",ss.mini())

