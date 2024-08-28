class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))  # Convert to string
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    # first solution using a hashmap

    def kthLast(self, k):
        if not self.head:
            raise Exception("aint no head")
        elementSet = {}
        index = 0
        n = self.head
        while n:
            index += 1
            elementSet[index] = n.data
            n = n.next
        return elementSet[(index+1) - k]

    # time: O(n)
    # space: O(n)

    # second solution that does it iteratively
    def kthtoLast(self, k):
        p1 = self.head
        p2 = self.head
        counter = 0
        while self.head:
            p1 = p1.next
            counter += 1
            if counter == k:
                break
        while p1 and p1.next:
            print("p1: ", p1.data)
            print("p2: ", p2.data)
            p1 = p1.next
            p2 = p2.next
        return p2.data
    # time: O(n)
    # space: O(1)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

ll = LinkedList()

ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(10)
ll.head.next.next.next = Node(31)
ll.head.next.next.next.next = Node(12)

print(ll.kthLast(2))

ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(10)
ll.head.next.next.next = Node(31)
ll.head.next.next.next.next = Node(12)

print(ll.kthtoLast(2))