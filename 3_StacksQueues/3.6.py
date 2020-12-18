# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly FIFO basis.
# People must adopt the oldest (based on arrival time) of all animals, or they select whether they prefer dog or cat (and take the oldest of that animal).
# Create the data structrues to maintain this system and implement operations such enqueue, dequeueAny, dequeueDog, dequeueCat.
# You may use the built in LinkedList data structure.

import unittest
from unittest.mock import patch

from linked_list import (Node, SLinkedList)

class Dog(Node):
    def __init__(self, name):
        Node.__init__(self, name)
        self.type = 'dog'

class Cat(Node):
    def __init__(self, name):
        Node.__init__(self, name)
        self.type = 'cat'

class AnimalShelter:
    def __init__(self):
        self.all_animals = SLinkedList()
    
    def enqueue(self, animal):
        self.all_animals.add_node((animal.data, animal.type))
    
    def enqueue_multi(self, *args):
        for x in args:
            self.enqueue(x)
    
    def dequeue(self):
        choice = ''
        while (type(choice) != int or choice not in [0, 1, 2]):
            choice = int(input("""
Choose an animal (enter a number):
0: Any
1: Dog
2: Cat
"""))

        choices = {0: 'any', 1: 'dog', 2: 'cat'}

        head = self.all_animals.head
        if choice == 0 or head.data[1] == choices[choice]:
            adopt = head
            self.all_animals.head = adopt.next
        else:
            adopt_temp = head
            while adopt_temp.next is not None and adopt_temp.next.data[1] != choices[choice]:
                adopt_temp = adopt_temp.next
            
            if adopt_temp.next is None:
                adopt = Node('No animal of that type')
            else:
                adopt = adopt_temp.next
                adopt_temp.next = adopt.next
        
        return adopt            

# Testing
class Tests(unittest.TestCase):

    def setUp(self):
        self.example = AnimalShelter()
        self.dog1 = Dog('Dorothy')
        self.dog2 = Dog ('Winnie')
        self.cat1 = Cat('Whiskers')
        self.example.enqueue_multi(self.dog1, self.cat1, self.dog2)

    # Mocking input 0 (any)
    @patch('builtins.input', return_value=0)
    def test_dequeue_any(self, input):
        self.assertEqual(self.example.dequeue().data, ('Dorothy', 'dog'))

    # Mocking input 1 (dog)
    @patch('builtins.input', return_value=1)
    def test_dequeue_dog(self, input):
        self.assertEqual(self.example.dequeue().data, ('Dorothy', 'dog'))
    
    # Mocking input 2 (cat)
    @patch('builtins.input', return_value=2)
    def test_dequeue_cat(self, input):
        self.assertEqual(self.example.dequeue().data, ('Whiskers', 'cat'))

if __name__ == '__main__':
    unittest.main()
