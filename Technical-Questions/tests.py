import unittest
from collections import deque
from graph41 import Node, Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        # Create nodes
        self.nodeA = Node("A")
        self.nodeB = Node("B")
        self.nodeC = Node("C")
        self.nodeD = Node("D")
        self.nodeE = Node("E")

        # Create graph
        self.graph = Graph()
        self.graph.nodes.extend([self.nodeA, self.nodeB, self.nodeC, self.nodeD])

        # Add children
        self.nodeA.children.extend([self.nodeB, self.nodeC])
        self.nodeB.children.append(self.nodeD)
        self.nodeC.children.append(self.nodeD)

    def test_path_to_nodes(self):
        # Assuming pathToNodes is implemented
        BFSpath = self.graph.pathToNodesBFS(self.graph, self.nodeA, self.nodeD)
        DFSpath = self.graph.pathToNodesDFS(self.graph, self.nodeA, self.nodeD)
        self.assertIsNotNone(BFSpath)
        self.assertIsNotNone(DFSpath)
        self.assertEqual(BFSpath, True)  # Example expected path
        self.assertEqual(DFSpath, True)
    
    def test_no_path(self):
        BFSpath = self.graph.pathToNodesBFS(self.graph, self.nodeA, self.nodeE)
        DFSpath = self.graph.pathToNodesDFS(self.graph, self.nodeA, self.nodeE)
        self.assertIsNotNone(BFSpath)
        self.assertIsNotNone(DFSpath)
        self.assertEqual(BFSpath, False)
        self.assertEqual(DFSpath, False)

if __name__ == '__main__':
    unittest.main()