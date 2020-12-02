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
    
    # Basic printing of the data of each node in the linked list
    def print_list(self):
        current = self.head
        print('')
        while current is not None:
            print(current.data)
            current = current.next

    # Pushing the data from each node into a list in order - for use with pretty_print and testing 
    def data_list(self):
        current = self.head    
        data_list = []
        while current is not None:
            data_list.append(current.data)
            current = current.next
        return data_list
    
    # Prints the data of each node in the linked list with arrows
    def pretty_print(self):
        pretty_list = map(str, self.data_list())
        print('\n' + ' -> '.join(pretty_list))

    # Add a new node with given data to the list
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

    # Add multiple new nodes with given data to the linked list
    def add_multi(self, *args):
        for data in args:
            self.add_node(data)
    
    # Delete a node from the list
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
    
    # Get the length of the linked list
    def length(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length
