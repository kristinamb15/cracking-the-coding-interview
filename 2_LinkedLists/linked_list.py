# Basic implementation of single linked list

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def add_next(self, data):
        end = Node(data)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

class SLinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def print_list(self):
        current = self.head
        print('')
        while current is not None:
            print(current.data)
            current = current.next
        
    def data_list(self):
        current = self.head    
        data_list = []
        while current is not None:
            data_list.append(current.data)
            current = current.next
        return data_list
    
    def pretty_print(self):
        pretty_list = map(str, self.data_list())
        print('\n' + ' -> '.join(pretty_list))

    def add_node(self, data):
        if self.head is None:
            new = Node(data)
            self.head = new
        else:
            current = self.head
            while current is not None:
                tail = current
                current = current.next
            tail.add_next(data)

    def add_multi(self, *args):
        for data in args:
            self.add_node(data)
    
    def delete_node(self, data):
        if self.head is None:
            return None
        
        current = self.head
        if current.data == data:
            return current.next
        
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return self.head
            current = current.next
        
        return self.head
    
    def length(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

""" node1 = Node(1)
node1.add_next(2)

mylist = SLinkedList(node1)
mylist.print_list()
mylist.add_node(3)
mylist.print_list()

mylist.delete_node(2)
mylist.pretty_print() """
