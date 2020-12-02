# Basic tree implementation

class Node: 
    def __init__(self, data, is_bin = False):
        self.data = data
        self.children = []
        self.is_bin = is_bin
        self.left = None
        self.right = None
    
    def get_children(self):
        if self.is_bin:
            if self.left is not None and self.right is not None:
                child_list = [f'Left: {self.left.data}', f'Right: {self.right.data}']
            elif self.left is None and self.right is not None:
                child_list = [f'Left: {self.left}', f'Right: {self.right.data}']               
            elif self.left is not None and self.right is None:
                child_list = [f'Left: {self.left.data}', f'Right: {self.right}']
            elif self.left is None and self.right is None:
                child_list = [child.data for child in self.children]
        else:
            child_list = [child.data for child in self.children]
        return child_list
    
    def add_child(self, node, left = False, right = False):
        self.children.append(node)
        if left:
            self.left = node
        if right:
            self.right = node
    
    def add_children(self, *nodes):
        for node in nodes:
            self.add_child(node)

    
class Tree:
    def __init__(self, root):
        self.root = root

    def add_node(self, parent, child_data):
        new_node = Node(child_data)
        parent.children.append(new_node)
    
    def add_multi(self, parent, *args):
        for x in args:
            self.add_node(parent, x)
    
    def in_order_traverse(self, node):
        if node is not None:
            if len(node.children) > 0:
                self.in_order_traverse(node.children[0])
            print(node.data)
            if len(node.children) > 1:
                self.in_order_traverse(node.children[1])
    
    def pre_order_traverse(self, node):
        if node is not None:
            print(node.data)
            if len(node.children) > 0:
                self.pre_order_traverse(node.children[0])
            if len(node.children) > 1:
                self.pre_order_traverse(node.children[1])
    
    def post_order_traverse(self, node):
        if node is not None:
            if len(node.children) > 0:
                self.post_order_traverse(node.children[0])
            if len(node.children) > 1:
                self.post_order_traverse(node.children[1])
            print(node.data)
    
    # Breadth-first print (first print I defined - probably excessive because I didn't use recursion)
    def print_bf(self):
        print(f'Root: {[self.root.data]}')
        parent_level = [self.root]
        i = 1

        while len(parent_level) > 0:
            level_data = [node.get_children() for node in parent_level]
            
            print(f'Level {i}: {level_data}')
            next_level = []
            empty = None

            for node in parent_level:
                for child in node.children:
                    next_level.append(child)

            for j in range(len(next_level)):
                if len(next_level[j].get_children()) == 0:
                    empty = True
                else:
                    empty = False
            i +=1

            if empty or empty is None:
                next_level = []
                
            parent_level = next_level

""" ex1_root = Node(1)
ex1_tree = Tree(ex1_root)
ex1_tree.add_multi(ex1_root, 2, 3)
ex1_tree.add_multi(ex1_root.children[0], 4, 5)
ex1_tree.add_multi(ex1_root.children[1], 6)
print('\nCustom defined print:')
ex1_tree.print_bf()
print('\nIn Order Traversal:')
ex1_tree.in_order_traverse(ex1_tree.root)
print('\nPre Order Traversal:')
ex1_tree.pre_order_traverse(ex1_tree.root)
print('\nPost Order Traversal:')
ex1_tree.post_order_traverse(ex1_tree.root) """

class Graph:
    def __init__(self, directed = False):
        self.edges = []
        self.nodes = set()
        self.directed = directed
    
    def add_edge(self, node1, node2):
        self.nodes.update({node1, node2})
        self.edges.append((node1, node2))
        if not self.directed:
            self.edges.append((node2, node1))
    
    def add_edge_multi(self, *args):
        for x in args:
            self.add_edge(x[0], x[1])

    def print_edges(self):
        for edge in self.edges:
            print(f'({edge[0].data}, {edge[1].data})')
    
    def set_state(self):
        nodes = set()
        for edge in self.edges:
            nodes.add(edge[0])
            nodes.add(edge[1])
        state = {node: False for node in nodes}
        return state



def populate_edges(graph, *nodes):
    for node in nodes:
        for child in node.children:
            graph.add_edge(node, child)
      
            