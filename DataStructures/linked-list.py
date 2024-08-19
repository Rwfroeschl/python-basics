
class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add(self, node):
        node.next = self.head
        self.head = node
    def add_end(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    def inbetween(self, target_node, new_node):
        if self.head is None:
            raise Exception("Empty")
        for node in self:
            if node.data == target_node.data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("No target")
    
    def delete(self, previous_node_data):
        if self.head is None:
            raise Exception("Empty")
        if self.head.data == previous_node_data:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == previous_node_data:
                previous_node.next = node.next
                node.next = None
                return
            previous_node = node
        
        raise Exception("No data")

                
            
        


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    

