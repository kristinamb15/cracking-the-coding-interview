# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly FIFO basis.
# People must adopt the oldest (based on arrival time) of all animals, or they select whether they prefer dog or cat (and take the oldest of that animal).
# Create the data structrues to maintain this system and implement operations such enqueue, dequeueAny, dequeueDog, dequeueCat.
# You may use the built in LinkedList data structure.

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

            

ex1 = AnimalShelter()
dog1 = Dog('Dorothy')
dog2 = Dog('Winnie')
cat1 = Cat('Whiskers')
# ex1.enqueue_multi(dog1, cat1, dog2)
# ex1.all_animals.pretty_print()
# adopt = ex1.dequeue()
# print(adopt.data)
# ex1.all_animals.pretty_print()

ex2 = AnimalShelter()
ex2.enqueue_multi(dog1, dog2)
adopt2 = ex2.dequeue()
print(adopt2.data)
ex2.all_animals.pretty_print()
