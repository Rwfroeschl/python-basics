class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)
    
    def append(self, data):
        if isinstance(data, LinkedList):
            if not self.head:
                self.head = data.head
            else:
                last = self.head
                while last.next:
                    last = last.next
                last.next = data.head
        else:
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def part(self, partition):
        slow, find = self.head, self.head
        while slow.next:
            if slow.data < partition:
                print ("less than partition: ", slow.data)
                slow = slow.next
                find = slow
            else:
                print ("greater than partition: ", slow.data)
                while find.next:
                    find = find.next
                    if find.data < partition:
                        find.data, slow.data = slow.data, find.data
                        print("breaking")
                        break
                if find.next == None:
                    return
                slow = slow.next
        # time : O(n^2)
        # space : O(1)
                
    def split(self, partition):
        smaller = LinkedList()
        greater = LinkedList()
        current = self.head
        while current:
            if current.data < partition:
                smaller.append(current.data)
            else:
                greater.append(current.data)
            current = current.next
        smaller.append(greater)
        
        self.head = smaller.head

    # time: O(n)
    # space: O(n)
            

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(2)
ll.append(1)

print(ll)

ll.part(5)

print("after partition: ", ll)

print("\nsecond example:\n")

l2 = LinkedList()
l2.append(3)
l2.append(6)
l2.append(2)
l2.append(6)
l2.append(7)
l2.append(2)

print("before partition: ",l2)

l2.split(5)

print("after partition: ", l2)