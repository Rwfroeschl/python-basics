from collections import deque
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


class Graph:
    def __init__(self):
        self.nodes = []

    # first solution using BFS 
    def pathToNodesBFS(self, graph, start, end):
        if not graph.nodes:
            raise Exception ("no nodes in the graph")
        queue = deque()
        visited = [False for _ in graph.nodes]
        visited[graph.nodes.index(start)] = True
        queue.append(start)
        print (visited)
        while queue:
            current = queue.popleft()
            print("current node: ",current.name)
            for node in current.children:
                print ("child in node: ", node.name)
                if node == end:
                    return True
                if visited[graph.nodes.index(node)] == False:
                    visited[graph.nodes.index(node)] = True
                print ("visited: ", visited)
                queue.append(node)
        return False

    
    def pathToNodesDFS(self, graph, start, end):
        if not graph.nodes:
            raise Exception ("no nodes in the graph")
        
        visited = [False for _ in graph.nodes]
        
        return self.dfs(graph, visited, start, end)
        
    def dfs(self, graph, visited, node, end):
        if not node:
            return False
        if node.name == end.name:
            return True
        print("index: ", graph.nodes.index(node))
        visited[graph.nodes.index(node)] = True
        
        for i in node.children:
            if not visited[graph.nodes.index(i)]:
                if self.dfs(graph, visited, i, end):
                    return True
        return False

    # Add a node to the graph
    def add_node(self, node):
        self.nodes.append(node)



# Example usage:
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")

# Adding adjacent nodes (edges)
nodeA.children.extend([nodeB, nodeC])
nodeB.children.append(nodeD)
nodeC.children.append(nodeD)


# Creating the graph and adding nodes to it
graph = Graph()
graph.add_node(nodeA)
graph.add_node(nodeB)
graph.add_node(nodeC)
graph.add_node(nodeD)
graph.pathToNodesBFS(graph, nodeA, nodeD)
print('\n')
graph.pathToNodesDFS(graph, nodeA, nodeD)

