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
    
    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    # when givin access to the head of the linked list
    def removeMiddle(self, node):
        previous_node = self.head
        current = self.head
        while current and current.next:
            current = current.next
            if current.data == node.data:
                previous_node.next = current.next
                current = previous_node.next
                return self.head
            previous_node = previous_node.next
        raise Exception("Never found the node in list")
    # time: O(n)
    # space: O(1)

    def removeMid(self, node):
        node.data = node.next.data
        node.next = node.next.next
    # time: O(n)
    # space: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



ll = LinkedList()

ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(10)
ll.head.next.next.next = Node(31)
ll.head.next.next.next.next = Node(12)

print(ll)

ll.removeMiddle(Node(10))
print(ll)
ll.removeMiddle(Node(31))
print(ll)


l2 = LinkedList()

l2.head = Node(1)
l2.head.next = Node(2)
l2.head.next.next = Node(10)
l2.head.next.next.next = Node(31)
l2.head.next.next.next.next = Node(12)
print("removeMid: ")
l2.removeMid(l2.find(10))
print(l2)
l2.removeMid(l2.find(31))
print(l2)