# 4.1 Route Between Nodes: Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.

from trees import (Node, Graph, populate_edges)

# Solution 1:
# O(NlogN) ???
def is_route(graph, node1, node2, state = None):
    if state is None:
        state = graph.set_state()
    #print({key.data: state[key] for key in state})
    print(node1.data, node2.data)
    if (node1, node2) in graph.edges:
        return True
    else:
        state[node1] = True
        for child in node1.children:
            if not state[child]:
                if is_route(graph, child, node2, state):
                    return True
                    break

a = Node('a')
b = Node('b')
c = Node('c')
r = Node('r')
s = Node('s')
t = Node('t')
a.add_children(b, r)
b.add_children(r, s, t)
c.add_children(t)
s.add_children(c)
ex1 = Graph(True)
populate_edges(ex1, a, b, c, r, s, t)
#ex1.print_edges()
print('\n')
print(is_route(ex1, s, t)) # True
r.add_child(b)
ex1.add_edge(r,b)
print(is_route(ex1, r, c))


