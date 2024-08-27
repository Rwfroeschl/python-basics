# remove duplicates in a linked list

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
    # First rendition / does not delete nodes
    def removeDup(self, head):
        if not head or not head.next:
            return head
        while head and head.next:
            curr = head.next
            while curr and curr.next:
                if head.data == curr.data:
                    self.remove(head, curr.data)
                curr = curr.next
            head = head.next
        return head
    
    def remove(self, head, data):
        if head.data == data:
            head = head.next
            return head
        previousNode = head
        while head:
            if head.data == data:
                previousNode.next = head.next
                head.next = None
                return head
            previousNode = head
            head = head.next

    # second rendition with modified code from copilot 
    def removeDupHash(self):
        if not self.head:
            raise Exception("no head :(")
        listSet = {}
        n = self.head
        while (n):
            print("data in while loop: ",n.data)
            if n.data in listSet:
                self.head = self.removeNodes(self.head, n.data)
            else:
                listSet[n.data] = 1
            n = n.next
        return self.head
    
    def removeNodes(self, head, data):
        while head and head.data == data:
            head = head.next
        
        current = head
        while current and current.next:
            if(current.next.data == data):
                print("data to be deleted: ", current.next.data)
                current.next = current.next.next
            else:
                current = current.next
        return head
    # Time: O(n^2)
    # space: O(n)

    # correct version with hash table 
    def deleteDups(self):
        listSet = {}
        previousNode = self.head
        n = self.head
        while n:
            if n.data in listSet:
                previousNode.next = n.next
            else:
                listSet[n.data] = 1
                previousNode = n
            n = n.next
        return self.head
    
    # time: O(N)
    # space: O(N)

    # solution using a two pointer approach

    def deletedup(self):
        current = self.head
        while current:
            runner = current
            while runner:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner.next
            current = current.next
        return self.head

        

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
ll.head.next = Node(3)
ll.head.next.next = Node(5)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(1)

ll.removeDup(ll.head)

print(ll)

l2 = LinkedList()
l2.head = Node(1)
l2.head.next = Node(3)
l2.head.next.next = Node(5)
l2.head.next.next.next = Node(3)
l2.head.next.next.next.next = Node(1)

l2.removeDupHash()
print(l2)

l3 = LinkedList()
l3.head = Node(1)
l3.head.next = Node(3)
l3.head.next.next = Node(5)
l3.head.next.next.next = Node(3)
l3.head.next.next.next.next = Node(1)

l3.deleteDups()
print(l3)

l4 = LinkedList()
l4.head = Node(1)
l4.head.next = Node(3)
l4.head.next.next = Node(5)
l4.head.next.next.next = Node(3)
l4.head.next.next.next.next = Node(1)

l4.deleteDups()
print(l4)