# 4.1 Route Between Nodes: Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.

from trees import (Node, Graph, populate_edges)

import unittest

# Solution 1:
# O(NlogN) ???
def is_route(graph, node1, node2, state = None):
    if state is None:
        state = graph.set_state()
    if (node1, node2) in graph.edges:
        return True
    else:
        state[node1] = True
        for child in node1.children:
            if not state[child]:
                if is_route(graph, child, node2, state):
                    return True
                    break

# Testing
class Tests(unittest.TestCase):

    def setUp(self):
        self.a = Node('a')
        self.b = Node('b')
        self.c = Node('c')
        self.r = Node('r')
        self.s = Node('s')
        self.t = Node('t')
        self.a.add_children(self.b, self.r)
        self.b.add_children(self.r, self.s, self.t)
        self.c.add_children(self.t)
        self.s.add_children(self.c)
        self.graph = Graph(True)
        populate_edges(self.graph, self.a, self.b, self.c, self.r, self.s, self.t)

    def test_is_route_true(self):
        self.assertTrue(is_route(self.graph, self.s, self.t))

    def test_is_route_false(self):
        self.assertFalse(is_route(self.graph, self.r, self.c))

if __name__ == '__main__':
    unittest.main()